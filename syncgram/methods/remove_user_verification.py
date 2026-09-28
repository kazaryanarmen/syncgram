from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def remove_user_verification(bot: TelegramBot, user_id: int) -> bool:
    """Removes verification from a user who is currently verified on behalf of the organization represented by the bot. Returns True on success."""
    payload = {
        'user_id': user_id,
    }
    return bot.request('removeUserVerification', payload)
