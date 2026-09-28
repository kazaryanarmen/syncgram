from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.owned_gifts import OwnedGifts
    from ..bot import TelegramBot

def get_business_account_gifts(bot: TelegramBot, business_connection_id: str, exclude_unsaved: bool | None = None, exclude_saved: bool | None = None, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_unique: bool | None = None, exclude_from_blockchain: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
    """Returns the gifts received and owned by a managed business account. Requires the can_view_gifts_and_stars business bot right. Returns OwnedGifts on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'exclude_unsaved': exclude_unsaved,
        'exclude_saved': exclude_saved,
        'exclude_unlimited': exclude_unlimited,
        'exclude_limited_upgradable': exclude_limited_upgradable,
        'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
        'exclude_unique': exclude_unique,
        'exclude_from_blockchain': exclude_from_blockchain,
        'sort_by_price': sort_by_price,
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getBusinessAccountGifts', payload)
