import json
import datetime

import settings
from slack_sdk.webhook import WebhookClient


def build_text(anniversary) -> str:
    today = datetime.date.today()
    name = anniversary["name"]
    tmp_date = datetime.datetime.strptime(anniversary["date"], '%Y-%m-%d')
    date = datetime.date(tmp_date.year, tmp_date.month, tmp_date.day)
    diff = today - date
    next_date = date.replace(year=date.year + 1)
    next_diff = next_date - today

    return f">>>*{name}* ( {date.strftime('%Y-%m-%d')} )\n\n経過日数\t{diff.days}日\n\n残り日数\t{next_diff.days}日"


def build_blocks(anniversaries) -> list:
    blocks = [
        {
            "type": "image",
            "image_url": "https://i.ytimg.com/vi/Mg8WdPJ_ATE/maxresdefault.jpg",
            "alt_text": "anniversary"
        }
    ]
    for anniversary in anniversaries:
        text = {
            "type": "section",
            "text": {
                "text": f"{build_text(anniversary)}",
                "type": "mrkdwn"
            }
        }
        blocks.append(text)

    return blocks


def main() -> None:
    anniversaries_file = open('anniversaries.json', 'r')
    anniversaries = json.load(anniversaries_file)

    webhook = WebhookClient(settings.WEBHOOK_URL)

    if not anniversaries:
        response = webhook.send(text='記念日を設定しましょ♪')
        assert response.status_code == 200
        assert response.body == "ok"
        return

    blocks = build_blocks(anniversaries)
    response = webhook.send(blocks=blocks)
    assert response.status_code == 200
    assert response.body == "ok"


if __name__ == '__main__':
    main()
