from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_chat_photo(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('deleteChatPhoto', payload)
