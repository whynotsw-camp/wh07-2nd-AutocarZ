/*
  라즈베리파이 ↔ 아두이노 (USB 시리얼)
  파이에서 'F','L','R','S' 중 1글자를 보내면
  - F : 앞으로
  - L : 좌회전 (왼쪽 느리게 / 오른쪽 빠르게)
  - R : 우회전 (오른쪽 느리게 / 왼쪽 빠르게)
  - S : 정지

  모터쉴드: Adafruit Motor Shield V1 (L293D)
  - 왼쪽 바퀴 : M1
  - 오른쪽 바퀴 : M4
*/

#include <AFMotor.h>

// --- 모터 객체 만들기 (쉴드의 M1, M4에 연결)
AF_DCMotor leftMotor(1);   // 왼쪽 바퀴 = M1
AF_DCMotor rightMotor(4);  // 오른쪽 바퀴 = M4

// --- 속도(0~255): 숫자가 클수록 빠름
const uint8_t BASE_SPEED  = 200;  // 기본 주행 속도
const uint8_t TURN_DELTA  = 140;   // 회전 시 속도 차이(좌/우 바퀴 차이)
const uint16_t WATCHDOG_MS = 500; // 마지막 명령 이후 이 시간 지나면 자동 정지(안전장치)

uint32_t lastCmdTime = 0;  // 마지막으로 명령 받은 시각(밀리초)

// --- 공통: 모터 정지 함수
void stopMotors() {
  leftMotor.setSpeed(0);
  rightMotor.setSpeed(0);
  leftMotor.run(RELEASE);
  rightMotor.run(RELEASE);
}

// --- 앞으로(양쪽 전진, 같은 속도)
void forward() {
  leftMotor.run(FORWARD);
  rightMotor.run(FORWARD);
  leftMotor.setSpeed(BASE_SPEED);
  rightMotor.setSpeed(BASE_SPEED);
}

// --- 좌회전(왼쪽 느리게, 오른쪽 빠르게)
//     ※ 너무 급하면 TURN_DELTA를 줄이세요.
void turnLeft() {
  leftMotor.run(FORWARD);
  rightMotor.run(FORWARD);
  uint8_t l = (BASE_SPEED > TURN_DELTA) ? (BASE_SPEED - TURN_DELTA) : 0;
  uint8_t r = min(255, BASE_SPEED + TURN_DELTA);
  leftMotor.setSpeed(l);
  rightMotor.setSpeed(r);
}

// --- 우회전(오른쪽 느리게, 왼쪽 빠르게)
void turnRight() {
  leftMotor.run(FORWARD);
  rightMotor.run(FORWARD);
  uint8_t l = min(255, BASE_SPEED + TURN_DELTA);
  uint8_t r = (BASE_SPEED > TURN_DELTA) ? (BASE_SPEED - TURN_DELTA) : 0;
  leftMotor.setSpeed(l);
  rightMotor.setSpeed(r);
}

void setup() {
  // 라즈베리파이 코드와 같은 속도로! (115200 보레이트)
  Serial.begin(115200);

  // 시작은 항상 안전하게 정지
  stopMotors();
}

void loop() {
  // 1) 파이에서 보낸 글자가 있으면 읽기
  if (Serial.available()) {
    char c = Serial.read();
    c = toupper(c);               // 대소문자 구분하지 않도록
    lastCmdTime = millis();       // 마지막 명령 시각 갱신

    switch (c) {
      case 'F': forward();   break;   // 앞으로
      case 'L': turnLeft();  break;   // 왼쪽으로
      case 'R': turnRight(); break;   // 오른쪽으로
      case 'S': stopMotors(); break;  // 정지
      default:
        // 다른 글자는 무시
        break;
    }

    // 버퍼에 남은 글자(연속 입력) 비우기 → 한 글자만 처리하려고
    while (Serial.available()) Serial.read();
  }

  // 2) 안전장치: 일정 시간 동안 명령이 없으면 자동 정지
  if (millis() - lastCmdTime > WATCHDOG_MS) {
    stopMotors();
  }
}
