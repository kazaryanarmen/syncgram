from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.user_profile_photos import UserProfilePhotos
    from ..bot import TelegramBot

def get_user_profile_photos(bot: TelegramBot, user_id: int, offset: int | None = None, limit: int | None = None) -> UserProfilePhotos:
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
    payload = {
        'user_id': user_id,
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getUserProfilePhotos', payload)
