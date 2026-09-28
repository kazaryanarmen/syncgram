from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def convert_gift_to_stars(bot: TelegramBot, business_connection_id: str, owned_gift_id: str) -> bool:
    """Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'owned_gift_id': owned_gift_id,
    }
    return bot.request('convertGiftToStars', payload)
