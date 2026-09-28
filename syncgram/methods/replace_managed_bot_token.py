from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def replace_managed_bot_token(bot: TelegramBot, user_id: int) -> str:
    """Use this method to revoke the current token of a managed bot and generate a new one. Returns the new token as String on success."""
    payload = {
        'user_id': user_id,
    }
    return bot.request('replaceManagedBotToken', payload)
