from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def verify_chat(bot: TelegramBot, chat_id: str | int, custom_description: str | None = None) -> bool:
    """Verifies a chat on behalf of the organization which is represented by the bot. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'custom_description': custom_description,
    }
    return bot.request('verifyChat', payload)
