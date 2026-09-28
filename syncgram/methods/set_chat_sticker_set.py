from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_chat_sticker_set(bot: TelegramBot, chat_id: str | int, sticker_set_name: str) -> bool:
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'sticker_set_name': sticker_set_name,
    }
    return bot.request('setChatStickerSet', payload)
