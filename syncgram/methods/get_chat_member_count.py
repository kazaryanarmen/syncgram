from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def get_chat_member_count(bot: TelegramBot, chat_id: str | int) -> int:
    """Use this method to get the number of members in a chat. Returns Integer on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('getChatMemberCount', payload)
