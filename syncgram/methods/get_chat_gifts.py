from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.owned_gifts import OwnedGifts
    from ..bot import TelegramBot

def get_chat_gifts(bot: TelegramBot, chat_id: str | int, exclude_unsaved: bool | None = None, exclude_saved: bool | None = None, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_from_blockchain: bool | None = None, exclude_unique: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
    """Returns the gifts owned by a chat. Returns OwnedGifts on success."""
    payload = {
        'chat_id': chat_id,
        'exclude_unsaved': exclude_unsaved,
        'exclude_saved': exclude_saved,
        'exclude_unlimited': exclude_unlimited,
        'exclude_limited_upgradable': exclude_limited_upgradable,
        'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
        'exclude_from_blockchain': exclude_from_blockchain,
        'exclude_unique': exclude_unique,
        'sort_by_price': sort_by_price,
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getChatGifts', payload)
