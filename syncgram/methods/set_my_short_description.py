from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_my_short_description(bot: TelegramBot, short_description: str | None = None, language_code: str | None = None) -> bool:
    """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."""
    payload = {
        'short_description': short_description,
        'language_code': language_code,
    }
    return bot.request('setMyShortDescription', payload)
