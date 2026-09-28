from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_message_reaction(bot: TelegramBot, chat_id: str | int, message_id: int, user_id: int | None = None, actor_chat_id: int | None = None) -> bool:
    """Use this method to remove a reaction from a message in a group or a supergroup chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'user_id': user_id,
        'actor_chat_id': actor_chat_id,
    }
    return bot.request('deleteMessageReaction', payload)
