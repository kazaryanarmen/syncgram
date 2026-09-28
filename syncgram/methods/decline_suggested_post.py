from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def decline_suggested_post(bot: TelegramBot, chat_id: int, message_id: int, comment: str | None = None) -> bool:
    """Use this method to decline a suggested post in a direct messages chat. The bot must have the 'can_manage_direct_messages' administrator right in the corresponding channel chat. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'comment': comment,
    }
    return bot.request('declineSuggestedPost', payload)
