from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_sticker import InputSticker
    from ..bot import TelegramBot

def create_new_sticker_set(bot: TelegramBot, user_id: int, name: str, title: str, stickers: list[InputSticker], sticker_type: str | None = None, needs_repainting: bool | None = None) -> bool:
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success."""
    payload = {
        'user_id': user_id,
        'name': name,
        'title': title,
        'stickers': stickers,
        'sticker_type': sticker_type,
        'needs_repainting': needs_repainting,
    }
    return bot.request('createNewStickerSet', payload)
