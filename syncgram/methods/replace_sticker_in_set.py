from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_sticker import InputSticker
    from ..bot import TelegramBot

def replace_sticker_in_set(bot: TelegramBot, user_id: int, name: str, old_sticker: str, sticker_: InputSticker) -> bool:
    """Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet, then setStickerPositionInSet. Returns True on success."""
    payload = {
        'user_id': user_id,
        'name': name,
        'old_sticker': old_sticker,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('replaceStickerInSet', payload, files=files if files else None)
