from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_messages(bot: TelegramBot, chat_id: str | int, message_ids: list[int]) -> bool:
    """Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_ids': message_ids,
    }
    return bot.request('deleteMessages', payload)
