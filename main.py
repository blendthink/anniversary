import argparse
import json
import datetime

import settings
from slack_sdk.webhook import WebhookClient


def build_message(anniversary) -> str:
    if anniversary is None:
        return '記念日を設定しましょ♪'

    today = datetime.date.today()
    name = anniversary["name"]
    tmp_date = datetime.datetime.strptime(anniversary["date"], '%Y-%m-%d')
    date = datetime.date(tmp_date.year, tmp_date.month, tmp_date.day)
    if date > today:
        return f"{name}に未来の日付が設定されちゃってる :pleading_face:"

    diff = today - date
    return f"『{name}』から {diff.days}日たちました :smiling_face_with_3_hearts:"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='wedding or .. etc')
    args = parser.parse_args()

    anniversaries_file = open('anniversaries.json', 'r')
    anniversaries = json.load(anniversaries_file)

    anniversary = next((item for item in anniversaries if item["key"] == args.type), None)

    webhook = WebhookClient(settings.WEBHOOK_URL)
    message = build_message(anniversary)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"


if __name__ == '__main__':
    main()
