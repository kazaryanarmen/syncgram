from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message import Message
    from ..bot import TelegramBot

def get_user_personal_chat_messages(bot: TelegramBot, user_id: int, limit: int) -> list[Message]:
    """Use this method to get the last messages from the personal chat (i.e., the chat currently added to their profile) of a given user. On success, an Array of Message objects is returned."""
    payload = {
        'user_id': user_id,
        'limit': limit,
    }
    return bot.request('getUserPersonalChatMessages', payload)
