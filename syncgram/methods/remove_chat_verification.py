from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def remove_chat_verification(bot: TelegramBot, chat_id: str | int) -> bool:
    """Removes verification from a chat that is currently verified on behalf of the organization represented by the bot. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('removeChatVerification', payload)
