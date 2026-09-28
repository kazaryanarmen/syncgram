from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.sticker_set import StickerSet
    from ..bot import TelegramBot

def get_sticker_set(bot: TelegramBot, name: str) -> StickerSet:
    """Use this method to get a sticker set. On success, a StickerSet object is returned."""
    payload = {
        'name': name,
    }
    return bot.request('getStickerSet', payload)
