import argparse
import settings
from slack_sdk.webhook import WebhookClient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='wedding or .. etc')
    args = parser.parse_args()
    webhook = WebhookClient(settings.WEBHOOK_URL)
    response = webhook.send(
        text=args.type
    )
    assert response.status_code == 200
    assert response.body == "ok"


if __name__ == '__main__':
    main()
