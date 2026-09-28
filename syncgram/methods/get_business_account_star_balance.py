from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.star_amount import StarAmount
    from ..bot import TelegramBot

def get_business_account_star_balance(bot: TelegramBot, business_connection_id: str) -> StarAmount:
    """Returns the amount of Telegram Stars owned by a managed business account. Requires the can_view_gifts_and_stars business bot right. Returns StarAmount on success."""
    payload = {
        'business_connection_id': business_connection_id,
    }
    return bot.request('getBusinessAccountStarBalance', payload)
