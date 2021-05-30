import argparse
from os import getenv
from slack_sdk.webhook import WebhookClient


def main() -> None:
    webhook_url = getenv('WEBHOOK_URL')
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='wedding or .. etc')
    args = parser.parse_args()
    print(args.type)
    webhook = WebhookClient(webhook_url)
    response = webhook.send(
        text=args.type
    )
    assert response.status_code == 200
    assert response.body == "ok"


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
