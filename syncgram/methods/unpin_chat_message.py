from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def unpin_chat_message(bot: TelegramBot, chat_id: str | int, business_connection_id: str | None = None, message_id: int | None = None) -> bool:
    """Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to unpin messages in groups and channels respectively. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'business_connection_id': business_connection_id,
        'message_id': message_id,
    }
    return bot.request('unpinChatMessage', payload)
