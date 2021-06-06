import argparse
import datetime
import json

from slack_sdk.webhook import WebhookClient

import settings
from data import Anniversary
from decoder import decode_anniversary


def build_first_text(anniversary: Anniversary) -> str:
    today = datetime.date.today()
    diff = today - anniversary.date
    return f'{anniversary.name}から {diff.days} 日'


def build_next_text(anniversary: Anniversary) -> str:
    today = datetime.date.today()
    next_date = anniversary.date.replace(year=anniversary.date.year + 1)
    next_diff = next_date - today
    return f'{anniversary.name}まで、あと {next_diff.days} 日'


def build_first_texts(anniversaries: [Anniversary]) -> str:
    messages = []
    for anniversary in anniversaries:
        message = build_first_text(anniversary)
        messages.append(message)

    messages.append('''\
がたちました :partying_face:

今日も両想いです :smiling_face_with_3_hearts:
''')

    return '\n'.join(messages)


def build_next_texts(anniversaries: [Anniversary]) -> str:
    messages = []
    for anniversary in anniversaries:
        message = build_next_text(anniversary)
        messages.append(message)
    messages.append('です :kissing_heart:')

    return '\n'.join(messages)


def build_blocks(anniversaries: [Anniversary]) -> list:
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    args = parser.parse_args()
    command_type = args.type

    message: str
    if command_type == 'first':
        message = build_first_texts(anniversaries)
    elif command_type == 'next':
        message = build_next_texts(anniversaries)
    else:
        message = 'キーが間違っています。'

    blocks = [
        {
            "type": "section",
            "text": {
                "text": f"{message}",
                "type": "mrkdwn"
            }
        }
    ]
    return blocks


def main() -> None:
    anniversaries_file = open('anniversaries.json', 'r')
    anniversaries: [Anniversary] = json.load(anniversaries_file, object_hook=decode_anniversary)

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
