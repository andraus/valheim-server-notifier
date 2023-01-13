BOT_VERSION = 'RANNI_WITCH_v0.3'

from typing import Optional

from lib.utils import read_logs
from lib.config import VALHEIM_LOG_PATH, DISCORD_WEBHOOK_URL, STEAM_API_ID, STEAM_API_ID
from event.matcher import resolve_event
from notifier.mapper import build_template
from notifier.discord import publish_event, publish_bot_init

def process_log(log: Optional[str] = None):
    if log is None:
        return

    event = resolve_event(log)
    if event:
        template = build_template(event)
        publish_event(DISCORD_WEBHOOK_URL, template)


if __name__ == '__main__':
    if VALHEIM_LOG_PATH is None:
        raise EnvironmentError('Missing <VALHEIM_LOG_PATH> envvar')

    if DISCORD_WEBHOOK_URL is None:
        raise EnvironmentError('Missing <DISCORD_WEBHOOK_URL> envvar')

    if STEAM_API_ID is None:
        raise EnvironmentError('Missing <STEAM_API_ID> envvar')

    publish_bot_init(DISCORD_WEBHOOK_URL, BOT_VERSION)

    logs = read_logs(path=VALHEIM_LOG_PATH)
    for log in logs:
        process_log(log)
