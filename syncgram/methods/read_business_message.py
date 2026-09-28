from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def read_business_message(bot: TelegramBot, business_connection_id: str, chat_id: int, message_id: int) -> bool:
    """Marks incoming message as read on behalf of a business account. Requires the can_read_messages business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
    }
    return bot.request('readBusinessMessage', payload)
