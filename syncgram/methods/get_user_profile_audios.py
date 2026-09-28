from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.user_profile_audios import UserProfileAudios
    from ..bot import TelegramBot

def get_user_profile_audios(bot: TelegramBot, user_id: int, offset: int | None = None, limit: int | None = None) -> UserProfileAudios:
    """Use this method to get a list of profile audios for a user. Returns a UserProfileAudios object."""
    payload = {
        'user_id': user_id,
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getUserProfileAudios', payload)
