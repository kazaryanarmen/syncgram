from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.forum_topic import ForumTopic
    from ..bot import TelegramBot

def create_forum_topic(bot: TelegramBot, chat_id: str | int, name: str, icon_color: int | None = None, icon_custom_emoji_id: str | None = None) -> ForumTopic:
    """Use this method to create a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator right. Returns information about the created topic as a ForumTopic object."""
    payload = {
        'chat_id': chat_id,
        'name': name,
        'icon_color': icon_color,
        'icon_custom_emoji_id': icon_custom_emoji_id,
    }
    return bot.request('createForumTopic', payload)
