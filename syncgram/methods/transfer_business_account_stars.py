from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def transfer_business_account_stars(bot: TelegramBot, business_connection_id: str, star_count: int) -> bool:
    """Transfers Telegram Stars from the business account balance to the bot's balance. Requires the can_transfer_stars business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'star_count': star_count,
    }
    return bot.request('transferBusinessAccountStars', payload)
