from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_short_description import BotShortDescription
    from ..bot import TelegramBot

def get_my_short_description(bot: TelegramBot, language_code: str | None = None) -> BotShortDescription:
    """Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success."""
    payload = {
        'language_code': language_code,
    }
    return bot.request('getMyShortDescription', payload)
