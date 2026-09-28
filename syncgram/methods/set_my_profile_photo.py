from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_profile_photo import InputProfilePhoto
    from ..bot import TelegramBot

def set_my_profile_photo(bot: TelegramBot, photo_: InputProfilePhoto) -> bool:
    """Changes the profile photo of the bot. Returns True on success."""
    payload = {
    }
    files = {
        'photo': photo_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setMyProfilePhoto', payload, files=files if files else None)
