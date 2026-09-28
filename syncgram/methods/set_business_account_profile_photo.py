from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_profile_photo import InputProfilePhoto
    from ..bot import TelegramBot

def set_business_account_profile_photo(bot: TelegramBot, business_connection_id: str, photo_: InputProfilePhoto, is_public: bool | None = None) -> bool:
    """Changes the profile photo of a managed business account. Requires the can_edit_profile_photo business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'is_public': is_public,
    }
    files = {
        'photo': photo_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setBusinessAccountProfilePhoto', payload, files=files if files else None)
