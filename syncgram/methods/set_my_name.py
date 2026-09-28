from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_my_name(bot: TelegramBot, name: str | None = None, language_code: str | None = None) -> bool:
    """Use this method to change the bot's name. Returns True on success."""
    payload = {
        'name': name,
        'language_code': language_code,
    }
    return bot.request('setMyName', payload)
