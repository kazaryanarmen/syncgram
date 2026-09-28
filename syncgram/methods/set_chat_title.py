from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_chat_title(bot: TelegramBot, chat_id: str | int, title: str) -> bool:
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'title': title,
    }
    return bot.request('setChatTitle', payload)
