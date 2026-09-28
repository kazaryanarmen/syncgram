from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def get_managed_bot_token(bot: TelegramBot, user_id: int) -> str:
    """Use this method to get the token of a managed bot. Returns the token as String on success."""
    payload = {
        'user_id': user_id,
    }
    return bot.request('getManagedBotToken', payload)
