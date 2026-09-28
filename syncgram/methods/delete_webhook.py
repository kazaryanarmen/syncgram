from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_webhook(bot: TelegramBot, drop_pending_updates: bool | None = None) -> bool:
    """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""
    payload = {
        'drop_pending_updates': drop_pending_updates,
    }
    return bot.request('deleteWebhook', payload)
