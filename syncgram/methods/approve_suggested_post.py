from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def approve_suggested_post(bot: TelegramBot, chat_id: int, message_id: int, send_date: int | None = None) -> bool:
    """Use this method to approve a suggested post in a direct messages chat. The bot must have the 'can_post_messages' administrator right in the corresponding channel chat. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'send_date': send_date,
    }
    return bot.request('approveSuggestedPost', payload)
