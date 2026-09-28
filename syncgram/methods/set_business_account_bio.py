from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_business_account_bio(bot: TelegramBot, business_connection_id: str, bio: str | None = None) -> bool:
    """Changes the bio of a managed business account. Requires the can_change_bio business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'bio': bio,
    }
    return bot.request('setBusinessAccountBio', payload)
