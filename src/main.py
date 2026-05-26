import os
import time
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def send_discord_alert(message: str):
    if not WEBHOOK_URL:
        print("DISCORD_WEBHOOK_URL 환경변수가 설정되지 않았습니다.")
        return

    data = {
        "content": message
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code in [200, 204]:
        print("Discord 알림 전송 성공")
    else:
        print("Discord 알림 전송 실패:", response.status_code, response.text)


def detect_pet():
    """
    실제 AI 탐지 코드를 연결하기 전 테스트용 함수입니다.
    나중에 HuskyLens, YOLO, 웹캠 탐지 코드로 교체하면 됩니다.
    """
    print("탐지 중...")
    time.sleep(2)

    # 테스트용으로 항상 True 반환
    return True


def main():
    print("AI Lost Pet Detector 시작")

    while True:
        detected = detect_pet()

        if detected:
            send_discord_alert("🐕 실종 반려동물로 의심되는 대상이 감지되었습니다!")
            time.sleep(10)

        time.sleep(1)


if __name__ == "__main__":
    main()
