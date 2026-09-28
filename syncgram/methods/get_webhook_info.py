from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.webhook_info import WebhookInfo
    from ..bot import TelegramBot

def get_webhook_info(bot: TelegramBot) -> WebhookInfo:
    """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
    payload = {
    }
    return bot.request('getWebhookInfo', payload)
