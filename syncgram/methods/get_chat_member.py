from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_member import ChatMember
    from ..bot import TelegramBot

def get_chat_member(bot: TelegramBot, chat_id: str | int, user_id: int) -> ChatMember:
    """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
    }
    return bot.request('getChatMember', payload)
