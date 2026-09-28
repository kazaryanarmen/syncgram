from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def unpin_all_general_forum_topic_messages(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('unpinAllGeneralForumTopicMessages', payload)
