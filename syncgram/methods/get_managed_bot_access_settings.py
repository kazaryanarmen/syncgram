from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_access_settings import BotAccessSettings
    from ..bot import TelegramBot

def get_managed_bot_access_settings(bot: TelegramBot, user_id: int) -> BotAccessSettings:
    """Use this method to get the access settings of a managed bot. Returns a BotAccessSettings object on success."""
    payload = {
        'user_id': user_id,
    }
    return bot.request('getManagedBotAccessSettings', payload)
