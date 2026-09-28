from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_full_info import ChatFullInfo
    from ..bot import TelegramBot

def get_chat(bot: TelegramBot, chat_id: str | int) -> ChatFullInfo:
    """Use this method to get up-to-date information about the chat. Returns a ChatFullInfo object on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('getChat', payload)
