# 🚍 AutocarZ - 자율주행 중 로드킬 안전 강화 및 자동 신고 서비스

# 🙋‍♂️🙋‍♀️ 팀원 소개

<table>
  <tr>
    <th>김지영</th>
    <th>이유석</th>
    <th>사석훈</th>
    <th>신윤서</th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/3c347b94-3b95-4d42-82ea-ee20c7dfcc45" width="100"/></td>
    <td><img src="https://github.com/user-attachments/assets/44c93308-1e79-4dc5-8ac0-a2dbd30785e8" width="100"/></td>
    <td><img src="https://github.com/user-attachments/assets/26c18044-d8ab-4b8b-a5a9-fb6ccd8b1071" width="100"/></td>
    <td><img src="https://github.com/user-attachments/assets/9b3cd675-6764-4b3e-bca3-7a356b20843f" width="100"/></td>
  </tr>
  <tr>
    <td>PM<br>임베디드 시스템 개발자<br>분석가</td>
    <td>팀원<br>임베디드 시스템 개발자<br>분석가</td>
    <td>팀원<br>Full-Stack 개발자<br>분석가</td>
    <td>팀원<br>FrontEnd<br>분석가</td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/jiyoung1634">
        <img src="https://img.shields.io/badge/GitHub-Link-black?logo=github&style=flat"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/LYSS-LGU">
        <img src="https://img.shields.io/badge/GitHub-Link-black?logo=github&style=flat"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/Clear-head">
        <img src="https://img.shields.io/badge/GitHub-Link-black?logo=github&style=flat"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/irisyshin">
        <img src="https://img.shields.io/badge/GitHub-Link-black?logo=github&style=flat"/>
      </a>
    </td>
  </tr>
</table>

---

# 프로젝트 기획서

## 1. 프로젝트 정의

- **목표**: 영상 기반으로 객체를 실시간 인식 및 상태를 분석하고, 특정 조건에 부합할 경우 사용자에게 신속하게 알림을 전송하는 지능형 관제 시스템 구축
- **주요 기능**:
  - 데이터 수집 및 전처리
  - 차선 인식·주행 제어
  - 야생동물/장애물 실시간 감지
  - 성능 평가 및 리포트 자동화

## 2. 주요 내용

- **프로젝트 기간**: 2025-08-25 ~ 2025-08-29
- **참여 인원**: [팀원 소개] 참고
- **데이터 사용처**: [로드킬 데이터 정보](https://www.data.go.kr/data/15045544/fileData.do), [야생동물 활동 영상 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?pageIndex=1&currMenu=115&topMenu=100&srchOptnCnd=OPTNCND001&searchKeyword=%EB%A1%9C%EB%93%9C%ED%82%AC&srchDetailCnd=DETAILCND001&srchOrder=ORDER001&srchPagePer=20&aihubDataSe=data&dataSetSn=645)


-------------

## 3. 일정 계획


| 작업 항목                      | 시작 날짜  | 종료 날짜  | 기간(일) |
| ------------------------------ | ---------- | ---------- | -------- |
| 프로젝트 기획서 및 계획서 작성 | 2025-08-25 | 2025-08-29 | 5        |
| 요구사항 정의서 작성           | 2025-08-25 | 2025-08-26 | 2        |
| WBS 작성                       | 2025-08-25 | 2025-08-26 | 2        |
| 데이터 수집 및 전처리          | 2025-08-25 | 2025-08-26 | 2        |
| MAP 시각화(통계 및 분석)       | 2025-08-26 | 2025-08-28 | 3        |
| 라즈베리파이 제어 코드 구현    | 2025-08-26 | 2025-08-29 | 4        |
| Dashboard 설계                 | 2025-08-25 | 2025-08-29 | 5        |
| 최종 검토 및 발표 준비         | 2025-08-28 | 2025-08-29 | 2        |
| 프로젝트 발표                  | 2025-08-29 | 2025-08-29 | 1        |

---

# 작업 분할 구조 (WBS)

<img width="937" height="684" alt="image" src="https://github.com/user-attachments/assets/88da226e-757b-4d08-9be8-762648a46fe1" />

---

# 요구사항 정의서

## 요구사항 정의서 상세 표

### 1. 기능 요구사항 (Functional Requirements)

| No | 구분 | 요구사항 ID | 요구사항 명 | 요구사항 상세 설명 | 담당자 | 비고 |
|---|---|---|---|---|---|---|
| 1 | 코어 엔진 | REQ-F-001 | 차선 인식 및 주행 | 라즈베리파이 환경에서 차선을 인식하고 차량이 차선을 따라 주행할 수 있도록 하는 기능 | 김지영, 이유석 | 초기 프로토타이핑 모델 기준 |
| 2 | 코어 엔진 | REQ-F-002 | 객체 자동 인식 | 영상에서 사전에 지정된 객체(사람, 자동차 등)를 자동으로 인식하고, 인식하지 못할 경우 자동 패스 처리 | 김지영, 이유석  | 인식 대상 객체 리스트 정의 필요 (정책) |
| 3 | 코어 엔진 | REQ-F-003 | 객체 상태 분석 | 인식된 객체가 '정지' 상태인지 '움직임' 상태인지 분류 | 김지영, 이유석  | '정지'와 '움직임'의 명확한 기준 정의 필요 (정책) |
| 4 | 코어 엔진 | REQ-F-004 | 객체 상태 재판단 | '움직임' 상태로 분류된 객체에 대해, 설정된 '다음 타이밍'에 다시 상태를 판단하는 로직 | 김지영, 이유석  | '다음 타이밍'의 시간 간격 정의 필요 (정책) |
| 5 | 코어 엔진 | REQ-F-005 | 객체 위치 식별 | 객체가 인식된 영상 내 위치(좌표)를 특정하고, 자주 출현하는 위치를 식별하는 기능 | 신윤서 | '자주' 출현하는 위치의 기준 정의 필요 (정책) |
| 6 | 데이터 | REQ-F-006 | 데이터 수집 및 저장 | 인식된 객체의 이미지와 관련 메타데이터(GPS, 시간 등)를 DB에 저장하여 향후 학습 데이터로 활용 | 김지영, 이유석  | DB 스키마 상세 정의 필요 (정책) |
| 7 | 시각화 | REQ-F-007 | 대시보드 구현 | 수집된 데이터를 기반으로 현황을 파악할 수 있는 대시보드 및 시연 영상 생성 |신윤서, 사석훈 |  |
| 8 | 시각화 | REQ-F-008 | 지도 연동 실시간 표시 | 인식된 객체의 GPS 정보를 Kakao MAP API와 연동하여 지도 위에 실시간으로 위치를 표시 | 사석훈 |  |
| 9 | 시각화 | REQ-F-009 | 통계 데이터 시각화 | 사건 발생 건수, 객체 종류별 빈도 등 주요 통계 데이터를 차트나 그래프 형태로 시각화 |신윤서, 사석훈 |  |
| 10 | 알림 | REQ-F-010 | 조건부 자동 알림 | 특정 조건(예: 정지 상태 1분 이상 지속) 발생 시, 영상 수신 서버에서 등록된 사용자에게 알림을 자동 전송 | 예정 | 사용자 시나리오 및 알림 형태 정의 필요 (정책) |
| 11 | 알림 | REQ-F-011 | 관리자 일괄 알림 | 관리자가 시스템을 통해 모든 사용자 혹은 특정 그룹에게 일괄적으로 알림(공지 등)을 발송하는 기능 | 예정 |  |

### 2. 비기능 요구사항 (Non-Functional Requirements)

| No | 구분 | 요구사항 ID | 요구사항 명 | 요구사항 상세 설명 | 요청부서 | 비고 |
|---|---|---|---|---|---|---|
| 12 | 성능 | REQ-N-001 | 객체 인식 속도 | 영상 프레임 수신 후 1초에 20번 라인(객체) 인식 및 상태 분석 처리 완료 | 김지영, 이유석  | 실시간 처리를 위한 기준 |
| 13 | 성능 | REQ-N-002 | 알림 전송 속도 | 라인(객체) 인식 후 이벤트 발생이 확정되면 3초 이내에 사용자에게 알림 전송 완료 | 김지영, 이유석 |  |
| 14 | 성능 | REQ-N-003 | 동시성 처리 | 다수의 카메라에서 이벤트가 동시에 발생해도 안정적으로 병렬 처리 가능해야 함 | 김지영, 이유석  | 시스템 실행 환경(서버 스펙 등)과 연관 (정책) |
| 15 | 보안 | REQ-N-004 | DB 접근 제어 | 데이터베이스는 외부에서 직접 접근할 수 없으며, 오직 API 서버를 통해서만 접근이 허용되어야 함 | 공통 |  |
| 16 | 확장성 | REQ-N-005 | 신규 객체 추가 | 향후 인식해야 할 새로운 종류의 객체를 시스템 수정 최소화하여 쉽게 추가할 수 있는 구조여야 함 | 공통 |  |

### 3. 정책 및 정의 필요 항목 (Policy & Definition Items)

| No | 구분 | 요구사항 ID | 요구사항 명 | 요구사항 상세 설명 | 요청부서 | 비고 |
|---|---|---|---|---|---|---|
| 17 | 정책 | REQ-P-001 | 인식 대상 객체 정의 | 인식할 '객체'의 범위를 명확히 정의 (예: 사람, 승용차, 트럭, 자전거, 반려동물 등 리스트업) | 공통 | 객체별 목표 인식률(성공 기준) 정의 필요 |
| 18 | 정책 | REQ-P-002 | 상태 판단 기준 정의 | • 정지: 몇 초 이상, 몇 픽셀 이내의 움직임을 '정지'로 볼 것인가?<br>• 움직임: 몇 픽셀 이상 좌표가 변해야 '움직임'으로 판단할 것인가? | 공통 |  |
| 19 | 정책 | REQ-P-003 | 재판단 간격('다음 타이밍') 정의 | 움직이는 객체를 얼마 간격(초)으로 다시 판단할 것인지 기준 정의 | 공통 |  |
| 20 | 정책 | REQ-P-004 | '자주 출현' 기준 정의 | '자주 인식되는 위치'를 판별하기 위한 기준 정의 (예: 하루 10회 이상, 1분 이상 체류 등) | 공통 |  |
| 21 | 정책 | REQ-P-005 | 영상/실행 환경 정의 | • 입력 영상: 영상 소스(IP 카메라 등), 해상도(FHD), 프레임(fps) 정의<br>• 실행 환경: 시스템 구동 환경(GPU 서버, 클라우드 등) 정의 | 공통 | 성능 요구사항(REQ-N-003)과 직접적인 연관 |
| 22 | 정책 | REQ-P-006 | DB 스키마 정의 | DB에 저장할 정보 구체화 (예: event_id, timestamp, object_type, gps_lat, gps_lon, image_path 등) | 공통 |  |
| 23 | 정책 | REQ-P-007 | 성공 기준(인식률) 정의 | 객체별로 목표로 하는 최소 인식 정확도(%) 정의 (예: 사람 99%, 자동차 95%) | 공통 |  |
| 24 | 정책 | REQ-P-008 | 사용자 시나리오 정의 | • 알림 수신 주체(보안팀, 관리자 등)는 누구인가?<br>• 알림 수신 후 기대하는 행동(CCTV 확인, 신고 등)은 무엇인가?<br>• 가장 효과적인 알림 형태(푸시, SMS 등)는 무엇인가? | 공통 |  |


> 요구사항 정의에 대해 자세한 내용은 📄 `요구사항_정의서.md/` 파일에서 확인하실 수 있습니다. 
---

# 프로젝트 설계서

## 1. 데이터 아키텍처 (ERD)

<img width="1300" height="615" alt="image" src="https://github.com/user-attachments/assets/e8e0d0fa-60d8-4874-881d-f90804542438" />


```sql
Table Event {
  event_id varchar(255) [pk, note: '이벤트의 고유 식별자 (기본 키)']
  lat float [not null, note: '이벤트 발생 위치의 위도']
  lon float [not null, note: '이벤트 발생 위치의 경도']
  detection_time datetime [not null, note: '이벤트 발생 시간']
  direction boolean [note: '상행/하행 정보']
  line_info varchar(255) [note: '관련 노선 정보 (e.g., 경부고속도로)']
  car_id varchar(255) [ref: > Car.car_id, note: '이벤트를 감지한 차량의 ID (Car 테이블 참조)']
  object_id varchar(255) [ref: > Object.object_id, note: '감지된 객체 ID (Object 테이블 참조)']
}

// Object: 감지될 수 있는 객체의 종류를 정의하는 테이블
Table Object {
  object_id varchar(255) [pk, note: '객체의 고유 식별자 (기본 키)']
  object_name varchar(255) [not null, note: '객체의 이름 (예: 고라니, 고양이, 낙하물)']
  risk_level int [note: '위험도 (1: 낮음, 2:보통, 3: 높음)']
}

// Car: 시스템에 등록된 차량 정보를 저장하는 테이블
Table Car {
  car_id varchar(255) [pk, note: '차량의 고유 식별자 (기본 키)']
  car_number varchar(125) [unique, not null, note: '차량 번호']
  car_type varchar(50) [note: '차종 (e.g., 승용차, 트럭, 버스)']
}

// ========================================
// 신고 및 알림 처리
// ========================================

// Report: 감지 이벤트를 기반으로 생성되는 신고 정보
Table Report {
  report_id varchar(255) [pk, note: '신고의 고유 식별자 (기본 키)']
  event_id varchar(255) [unique, ref: > Event.event_id, note: '원본 이벤트 ID']
  report_time datetime [not null, note: '신고 접수 시간']
  status report_status [not null, default: 'received', note: '신고 처리 상태']
  report_image_url varchar(255) [note: '증빙 객체 이미지 URL']
}

// Authority: 신고를 전달받는 관계 기관 정보
Table Authority {
  authority_id varchar(255) [pk, note: '기관의 고유 식별자 (기본 키)']
  name varchar(225) [not null, note: '기관명 (e.g., 한국도로공사, 서초구청)']
  type authority_type [not null, note: '기관 종류']
  contact varchar(255) [note : '연락처 또는 API Endpoint']
}

// ReportForwarding: 특정 신고가 어떤 기관에 전달되었는지 기록 (N:M 관계)
Table ReportForwarding {
  forwarding_id varchar(255) [pk, note: '전달 내역 고유 식별자 (기본 키)']
  report_id varchar(255) [ref: > Report.report_id, not null]
  authority_id varchar(255) [ref: > Authority.authority_id, not null]
  forwarding_time datetime [not null, note: '기관에 전달된 시간']
}

// Alert: 인근 운전자에게 발송되는 알림 정보
Table Alert {
  alert_id varchar(255) [pk, note: '알림의 고유 식별자 (기본 키)']
  report_id varchar(255) [ref: > Report.report_id, not null, note: '어떤 신고에 대한 알림인지']
  target_car_id varchar(255) [ref: > Car.car_id, not null, note: '알림을 수신한 차량 ID']
  alert_time datetime [not null, note: '알림 발송 시간']
  is_checked boolean [default: false, note: '수신 차량의 확인 여부']
}

```


## 2. 기술 스택

- 사용 언어 : ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) 
![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=C&logoColor=white)


### **📊 데이터 분석 및 처리**
- 라이브러리 : ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/Numpy-013243?style=flat&logo=numpy&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=flat&logo=opencv&logoColor=white)

### **📈 시각화 도구**
-  ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-1E3C72?style=flat) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)


### **🤖 AI / ML**
- 모델 : ![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=flat&logo=YOLO&logoColor=black) ![ResNet50](https://img.shields.io/badge/ResNet50-FF5959?style=flat)
- 프레임워크 : ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
-  머신러닝 : ![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
-  하드웨어: ![arduino](https://img.shields.io/badge/arduino-00878F?style=flat&logo=arduino&logoColor=white)
![raspberrypi](https://img.shields.io/badge/raspberrypi-A22846?style=flat&logo=raspberrypi&logoColor=white)

### 🗃️ 인프라 & 배포 & 서버
- 클라우드 : ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white) ![EC2](https://img.shields.io/badge/EC2-FF9900?style=flat&logo=amazon-ec2&logoColor=white)
- 데이터베이스 : <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white" />
- 서버 : ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
  

---


# 설계 이미지

## 1-1. 시스템 아키텍처

<img width="1046" height="693" alt="image" src="https://github.com/user-attachments/assets/2df2fba3-dcc2-456d-ba5f-3d6945ce7f9f" />


## 1-2 시스템 흐름도

<img width="804" height="774" alt="image" src="https://github.com/user-attachments/assets/8f395fcc-3ee4-4478-a191-0fb0e2f2ac42" />



## 1-3 대시보드

<img width="1105" height="528" alt="image" src="https://github.com/user-attachments/assets/25f55038-564f-4707-aab1-89c4ab98cf11" />

---


# 프로젝트 주요 결과 요약

- **성과**:
  - 데이터 수집 및 전처리 후 DB 적재
  - MAP 핀포인트, 마커 필터, 통계량 대시보드 구현
  - 라인트레이싱 주행 성공

