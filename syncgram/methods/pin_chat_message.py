from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def pin_chat_message(bot: TelegramBot, chat_id: str | int, message_id: int, business_connection_id: str | None = None, disable_notification: bool | None = None) -> bool:
    """Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to pin messages in groups and channels respectively. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'business_connection_id': business_connection_id,
        'disable_notification': disable_notification,
    }
    return bot.request('pinChatMessage', payload)
