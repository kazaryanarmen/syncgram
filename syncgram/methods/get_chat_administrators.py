from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_member import ChatMember
    from ..bot import TelegramBot

def get_chat_administrators(bot: TelegramBot, chat_id: str | int, return_bots: bool | None = None) -> list[ChatMember]:
    """Use this method to get a list of administrators in a chat. Returns an Array of ChatMember objects."""
    payload = {
        'chat_id': chat_id,
        'return_bots': return_bots,
    }
    return bot.request('getChatAdministrators', payload)
