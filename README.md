# AI Lost Pet Detector 🐕

AI 카메라를 활용해 실종 반려동물 또는 유기견을 탐지하고, Discord로 실시간 알림을 보내는 프로젝트입니다.

## 프로젝트 소개
이 프로젝트는 지역 사회에서 발생하는 실종 반려동물 문제와 유기견 배회 문제를 해결하기 위해 기획되었습니다.

카메라가 특정 동물이나 대상을 인식하면 Python 프로그램이 이를 처리하고, Discord Webhook을 통해 관리자에게 알림을 전송합니다.

## 제작 동기
동네 커뮤니티에서 유기견 목격 글을 자주 보며, 빠른 알림 시스템이 있다면 사고를 줄이고 보호자에게 더 빨리 정보를 전달할 수 있다고 생각했습니다.

## 주요 기능
- 카메라를 통한 대상 탐지
- HuskyLens 또는 웹캠 기반 인식
- 탐지 시 Discord Webhook 알림 전송
- Raspberry Pi 기반 독립 실행 가능
- YOLO 모델 확장 가능

## 사용 기술
- Python
- Raspberry Pi
- HuskyLens
- Webcam
- Discord Webhook
- YOLO

## 시스템 구조
```txt
Camera / HuskyLens
        ↓
Python Detection Program
        ↓
Discord Webhook Alert
        ↓
User / Community Notification
