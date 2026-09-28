from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def remove_my_profile_photo(bot: TelegramBot) -> bool:
    """Removes the profile photo of the bot. Requires no parameters. Returns True on success."""
    payload = {
    }
    return bot.request('removeMyProfilePhoto', payload)
