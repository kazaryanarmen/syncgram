from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def ban_chat_sender_chat(bot: TelegramBot, chat_id: str | int, sender_chat_id: int) -> bool:
    """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'sender_chat_id': sender_chat_id,
    }
    return bot.request('banChatSenderChat', payload)
