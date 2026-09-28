from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.mask_position import MaskPosition
    from ..bot import TelegramBot

def set_sticker_mask_position(bot: TelegramBot, sticker_: str, mask_position: MaskPosition | None = None) -> bool:
    """Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success."""
    payload = {
        'mask_position': mask_position,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setStickerMaskPosition', payload, files=files if files else None)
