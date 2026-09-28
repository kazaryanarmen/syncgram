from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def edit_forum_topic(bot: TelegramBot, chat_id: str | int, message_thread_id: int, name: str | None = None, icon_custom_emoji_id: str | None = None) -> bool:
    """Use this method to edit name and icon of a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_thread_id': message_thread_id,
        'name': name,
        'icon_custom_emoji_id': icon_custom_emoji_id,
    }
    return bot.request('editForumTopic', payload)
