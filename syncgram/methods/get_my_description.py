from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_description import BotDescription
    from ..bot import TelegramBot

def get_my_description(bot: TelegramBot, language_code: str | None = None) -> BotDescription:
    """Use this method to get the current bot description for the given user language. Returns BotDescription on success."""
    payload = {
        'language_code': language_code,
    }
    return bot.request('getMyDescription', payload)
