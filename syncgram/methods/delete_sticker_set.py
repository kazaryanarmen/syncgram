from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_sticker_set(bot: TelegramBot, name: str) -> bool:
    """Use this method to delete a sticker set that was created by the bot. Returns True on success."""
    payload = {
        'name': name,
    }
    return bot.request('deleteStickerSet', payload)
