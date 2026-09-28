from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.owned_gifts import OwnedGifts
    from ..bot import TelegramBot

def get_user_gifts(bot: TelegramBot, user_id: int, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_from_blockchain: bool | None = None, exclude_unique: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
    """Returns the gifts owned and hosted by a user. Returns OwnedGifts on success."""
    payload = {
        'user_id': user_id,
        'exclude_unlimited': exclude_unlimited,
        'exclude_limited_upgradable': exclude_limited_upgradable,
        'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
        'exclude_from_blockchain': exclude_from_blockchain,
        'exclude_unique': exclude_unique,
        'sort_by_price': sort_by_price,
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getUserGifts', payload)
