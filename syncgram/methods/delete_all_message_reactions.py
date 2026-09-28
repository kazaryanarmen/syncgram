from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_all_message_reactions(bot: TelegramBot, chat_id: str | int, user_id: int | None = None, actor_chat_id: int | None = None) -> bool:
    """Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'actor_chat_id': actor_chat_id,
    }
    return bot.request('deleteAllMessageReactions', payload)
