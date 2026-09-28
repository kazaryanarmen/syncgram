from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def remove_business_account_profile_photo(bot: TelegramBot, business_connection_id: str, is_public: bool | None = None) -> bool:
    """Removes the current profile photo of a managed business account. Requires the can_edit_profile_photo business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'is_public': is_public,
    }
    return bot.request('removeBusinessAccountProfilePhoto', payload)
