# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# 카메라로 바닥 아래쪽(ROI)을 본다
# → 흰색 테이프만 골라낸다(마스크)
# → 테이프가 화면 가로 중 어디(왼/가운데/오른쪽)에 많은지 본다
# → 그 위치에 따라 'L'(좌회전), 'R'(우회전), 'F'(직진), 'S'(정지)를
#    USB 시리얼로 아두이노에게 한 글자 전송한다.
# ------------------------------------------------------------

import cv2
import numpy as np
import time
import glob # 파일 이름을 찾을 때 쓰는 도구
import serial

# ① 카메라 열기 (0번 = 첫 번째 카메라, 보통 /dev/video0)
cap = cv2.VideoCapture(0)
# 해상도를 너무 높게 하면 느려짐 → 640x480 정도가 실시간에 적당
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ② HSV에서 "흰색" 범위(조명에 따라 살짝 조정)
#    H(색상)는 상관 없음(0~179 전체 허용)
#    S(채도)는 낮게(무채색에 가깝게)
#    V(밝기)는 높게(밝은 것만)
LOWER = np.array([0,   0, 200], dtype=np.uint8)   # 아래쪽 경계: S 낮고 V 밝음
UPPER = np.array([179, 60, 245], dtype=np.uint8)  # 위쪽 경계: 필요하면 S=80까지 올리기


def extract_white_mask(bgr_roi):
    """
    bgr_roi: 화면 아래쪽(ROI) 잘라낸 색상 영상 (BGR)
    동작: BGR → HSV 변환 → 흰색 영역만 255(흰), 나머지는 0(검정)으로 만든 뒤
          작은 점 노이즈를 블러/모폴로지로 줄인다.
    결과: 흑백(이진) 마스크 반환
    """
    hsv = cv2.cvtColor(bgr_roi, cv2.COLOR_BGR2HSV)     # 색공간 BGR → HSV    
    mask = cv2.inRange(hsv, LOWER, UPPER)              # 범위 안이면 255, 아니면 0
    mask = cv2.GaussianBlur(mask, (5,5), 0)            # 점점이 노이즈 부드럽게
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))  # 5x5 네모 도장
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)      # 열기(침식→팽창)로 찌꺼기 제거
    return mask

# ③ 아두이노와 USB 시리얼 연결 열기
def open_serial():
    """
    /dev/ttyACM0(우노·레오나르도 계열), /dev/ttyUSB0(일부 보드/어댑터)
    둘 다 검사해서 열어 본다. 아두이노 스케치의 Serial.begin(115200)과 속도를 맞춘다.
    """
    candidates = sorted(list(glob.glob("/dev/ttyACM*")) + list(glob.glob("/dev/ttyUSB*"))) # 연결된 아두이노 찾기
    for dev in candidates:
        try:
            ser = serial.Serial(dev, 115200, timeout=0.01) # 아두이노에 연결(속도:115200, 연결을 시도할 때 너무 오래 기다리지 않도록 0.01초만 기다려)
            time.sleep(2.0)  # 아두이노가 자동 리셋되므로 2초 대기
            print("Serial connected:", dev)
            return ser
        except Exception as e: # 연결 실패
            print("Skip", dev, e)
    print("No serial port found. Run without Arduino.")
    return None

ser = open_serial()

# ④ 제어 파라미터(필요시 조정)
DEADBAND = 20          # 가운데에서 좌우 ±20픽셀 이내면 "직진(F)"로 간주
NOISE_MIN = 20000      # 흰색 합계가 이 값보다 작으면 "차선 못 봄"으로 간주 → S(정지)
SEND_HZ   = 20         # 1초에 최대 20번만 명령 전송(너무 자주 보내지 않기)
last_send = 0
last_cmd  = 'S'

def decide_command(mask_width, peak_x, center_x): # 자동차가 어디로 가야 할지 결정하는 함수   
    """
    peak_x: 흰색이 가장 많은 x 위치(ROI 기준)
    center_x: 화면 가운데 x (w//2)
    반환: 'F','L','R','S' 중 하나
    """
    if peak_x is None:      # 흰색을 거의 못 봤다 → 정지
        return 'S'
    
    err = peak_x - center_x # +면 오른쪽으로 치우쳤고, -면 왼쪽으로 치우침
    if abs(err) <= DEADBAND:
        return 'F'          # 거의 중앙 → 직진
    return 'R' if err < 0 else 'L'   # 왼쪽이면 L, 오른쪽이면 R

def send_cmd(cmd):
    """같은 글자를 너무 자주 보내지 않도록 제한해서 전송"""
    global last_cmd, last_send, ser
    now = time.time() # 지금 현재 시간
    if now - last_send < 1.0 / SEND_HZ: # now가 마지막으로 명령을 보낸 시간보다 빠르면 명령을 보내지 않음
        return
    print("CMD:", cmd)              # 보기용 출력
    if ser is not None: # ser가 잘 연결되었을 때
        try:
            ser.write(cmd.encode('ascii'))  # 한 글자 전송
        except Exception as e:
            print("Serial write fail:", e)
    last_cmd = cmd # 마지막 명령을 지금 명령으로 바꾸기
    last_send = now # 마지막 시간을 지금 시간으로 바꾸기

# ⑤ 메인 루프(계속 반복)
while True:
    ok, frame = cap.read()       # 카메라에서 한 장 읽기
    if not ok:
        break

    # 화면 아래쪽만 보기(ROI=관심영역). 속도↑, 엉뚱한 물체↓
    h, w, _ = frame.shape
    roi_top = int(h * 0.6)       # 세로 60% 지점 → 그 아래 40%를 사용
    roi = frame[roi_top:, :]     # [행: roi_top~끝, 열: 전체]

    # 흰색 차선만 남긴 흑백 마스크 만들기
    mask = extract_white_mask(roi)

    # 가로 방향으로 흰색이 얼마나 있는지 합산(열별 합계) → 히스토그램
    col_sum = mask.sum(axis=0)   # shape: (w,) # mask이미지에서 세로줄에 있는 흰색(255) 양을 더하기
    total_white = int(col_sum.sum()) # 모든 세로줄의 흰색 양을 더하기 -> 클수록 차선을 잘 보고 있다고 해석

    # 두 차선의 중앙을 찾는 부분
    # 흰색 총량이 너무 적으면(=차선 못 봄) peak_x는 None
    peak_x = None
    if total_white > NOISE_MIN:
        peak_x = int(col_sum.argmax()) # 흰색이 가장 많은 위치(=차선 위치)
        # 화면을 반으로 나누어 왼쪽과 오른쪽 차선을 각각 찾음
        center_x = w // 2
        left_hist = col_sum[:center_x]   # 히스토그램의 왼쪽 절반
        right_hist = col_sum[center_x:]  # 히스토그램의 오른쪽 절반
        # 각 절반에서 흰색이 가장 많은 위치를 찾습니다.
        left_peak_x = left_hist.argmax()
        # 오른쪽 위치는 center_x를 더해주어야 전체 화면 기준 좌표가 됩니다.
        right_peak_x = right_hist.argmax() + center_x
        # 두 차선 위치의 평균을 내어 도로의 중앙을 계산
        lane_center_x = (left_peak_x + right_peak_x) // 2
        # 계산된 중앙 위치를 최종 목표 지점(peak_x)로 설정
        peak_x = int(lane_center_x)

    # 가운데와 비교해서 F/L/R/S 결정
    center_x = w // 2
    cmd = decide_command(w, peak_x, center_x) # F,L,R,S 중 하나를 결정해서 cmd에 담기
    send_cmd(cmd) # cmd를 아두이노에게 보내기

    # ---------- 보기용 그림(원본+표식) ----------
    vis = frame.copy()
    # ROI 경계선(초록 가로선): 여기 아래만 분석한다는 표시
    cv2.line(vis, (0, roi_top), (w-1, roi_top), (0, 255, 0), 2)
    # 가운데 파란선, 검출된 피크 빨간점
    if peak_x is not None: # 차선을 잘 찾았다면
        cv2.line(vis, (center_x, roi_top), (center_x, h-1), (255, 0, 0), 1)   # 파란 선(화면 정중앙)
        cv2.circle(vis, (peak_x, roi_top+10), 6, (0, 0, 255), -1)             # 빨간 원(검출 위치, 찾은 흰색 차선(peak_x))

    cv2.imshow("camera", vis)   # 원본+표식
    cv2.imshow("mask", mask)    # 흰색만 남긴 마스크(ROI)

    # 키보드: q=종료, s/f/l/r는 수동 테스트(아두이노 연결 시)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key in (ord('s'), ord('S')):
        send_cmd('S')
    elif key == ord('f'):
        send_cmd('F')
    elif key == ord('l'):
        send_cmd('L')
    elif key == ord('r'):
        send_cmd('R')

# 정리
cap.release()
cv2.destroyAllWindows()
if ser is not None:
    ser.close()
