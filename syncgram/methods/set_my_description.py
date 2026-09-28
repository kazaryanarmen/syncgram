from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_my_description(bot: TelegramBot, description: str | None = None, language_code: str | None = None) -> bool:
    """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success."""
    payload = {
        'description': description,
        'language_code': language_code,
    }
    return bot.request('setMyDescription', payload)
