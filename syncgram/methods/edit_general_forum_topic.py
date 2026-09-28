from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def edit_general_forum_topic(bot: TelegramBot, chat_id: str | int, name: str) -> bool:
    """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'name': name,
    }
    return bot.request('editGeneralForumTopic', payload)
