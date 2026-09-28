from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def close_forum_topic(bot: TelegramBot, chat_id: str | int, message_thread_id: int) -> bool:
    """Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_thread_id': message_thread_id,
    }
    return bot.request('closeForumTopic', payload)
