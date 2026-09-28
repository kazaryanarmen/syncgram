from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def unpin_all_chat_messages(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method to clear the list of pinned messages in a chat. In private chats and channel direct messages chats, no additional rights are required to unpin all pinned messages. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to unpin all pinned messages in groups and channels respectively. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('unpinAllChatMessages', payload)
