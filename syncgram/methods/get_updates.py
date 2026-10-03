from __future__ import annotations
from typing import TYPE_CHECKING, List, Any

if TYPE_CHECKING:
    from ..objects.update import Update
    from ..bot import TelegramBot

def get_updates(bot: TelegramBot, offset: int | None = None, limit: int | None = None, timeout: int | None = None, allowed_updates: list[str] | None = None) -> list[Any]:
    """Use this method to receive incoming updates using long polling. Returns a flat list of Update objects or dicts."""
    payload = {
        'offset': offset,
        'limit': limit,
        'timeout': timeout,
        'allowed_updates': allowed_updates,
    }
    response = bot.request('getUpdates', payload)

    if isinstance(response, dict):
        raw_result = response.get('result', [])
    elif isinstance(response, list):
        raw_result = response
    else:
        raw_result = []

    flat_updates = []
    for item in raw_result:
        if isinstance(item, list):
            flat_updates.extend(item)
        else:
            flat_updates.append(item)

    from ..objects.update import Update
    processed_updates = []
    for item in flat_updates:
        if isinstance(item, dict):
            try:
                processed_updates.append(Update.from_dict(item))
            except Exception:
                processed_updates.append(item)
        else:
            processed_updates.append(item)

    return processed_updates