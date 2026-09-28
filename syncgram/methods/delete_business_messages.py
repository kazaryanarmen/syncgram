from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_business_messages(bot: TelegramBot, business_connection_id: str, message_ids: list[int]) -> bool:
    """Delete messages on behalf of a business account. Requires the can_delete_sent_messages business bot right to delete messages sent by the bot itself, or the can_delete_all_messages business bot right to delete any message. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'message_ids': message_ids,
    }
    return bot.request('deleteBusinessMessages', payload)
