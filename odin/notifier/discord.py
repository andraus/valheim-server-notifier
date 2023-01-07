from requests import post

from . import Template


def publish_event(webhook_url: str, event: Template):
    post(
        webhook_url,
        json=event.get_payload(),
        headers={'Content-Type': 'application/json'}
    )

def publish_bot_init(webhook_url: str, botVersion: str):
    post(
        webhook_url,
        json={'content': f'I am the witch Renna `[{botVersion}]`.'},
        headers={'Content-Type': 'application/json'}
    )
