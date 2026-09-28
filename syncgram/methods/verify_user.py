from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def verify_user(bot: TelegramBot, user_id: int, custom_description: str | None = None) -> bool:
    """Verifies a user on behalf of the organization which is represented by the bot. Returns True on success."""
    payload = {
        'user_id': user_id,
        'custom_description': custom_description,
    }
    return bot.request('verifyUser', payload)
