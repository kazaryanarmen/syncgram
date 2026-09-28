from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_name import BotName
    from ..bot import TelegramBot

def get_my_name(bot: TelegramBot, language_code: str | None = None) -> BotName:
    """Use this method to get the current bot name for the given user language. Returns BotName on success."""
    payload = {
        'language_code': language_code,
    }
    return bot.request('getMyName', payload)
