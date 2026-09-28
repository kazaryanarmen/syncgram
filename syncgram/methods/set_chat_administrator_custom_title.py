from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_chat_administrator_custom_title(bot: TelegramBot, chat_id: str | int, user_id: int, custom_title: str) -> bool:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'custom_title': custom_title,
    }
    return bot.request('setChatAdministratorCustomTitle', payload)
