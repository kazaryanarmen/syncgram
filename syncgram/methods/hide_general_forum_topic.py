from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def hide_general_forum_topic(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('hideGeneralForumTopic', payload)
