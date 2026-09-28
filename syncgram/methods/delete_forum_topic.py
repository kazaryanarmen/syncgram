from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_forum_topic(bot: TelegramBot, chat_id: str | int, message_thread_id: int) -> bool:
    """Use this method to delete a forum topic along with all its messages in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_thread_id': message_thread_id,
    }
    return bot.request('deleteForumTopic', payload)
