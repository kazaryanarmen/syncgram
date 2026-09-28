from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def leave_chat(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('leaveChat', payload)
