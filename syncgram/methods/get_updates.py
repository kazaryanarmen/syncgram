from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.update import Update
    from ..bot import TelegramBot

def get_updates(bot: TelegramBot, offset: int | None = None, limit: int | None = None, timeout: int | None = None, allowed_updates: list[str] | None = None) -> list[Update]:
    """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects."""
    payload = {
        'offset': offset,
        'limit': limit,
        'timeout': timeout,
        'allowed_updates': allowed_updates,
    }
    return bot.request('getUpdates', payload)
