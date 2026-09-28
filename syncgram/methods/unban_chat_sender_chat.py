from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def unban_chat_sender_chat(bot: TelegramBot, chat_id: str | int, sender_chat_id: int) -> bool:
    """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'sender_chat_id': sender_chat_id,
    }
    return bot.request('unbanChatSenderChat', payload)
