from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_chat_description(bot: TelegramBot, chat_id: str | int, description: str | None = None) -> bool:
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'description': description,
    }
    return bot.request('setChatDescription', payload)
