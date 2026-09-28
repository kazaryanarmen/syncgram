from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_sticker_from_set(bot: TelegramBot, sticker_: str) -> bool:
    """Use this method to delete a sticker from a set created by the bot. Returns True on success."""
    payload = {
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('deleteStickerFromSet', payload, files=files if files else None)
