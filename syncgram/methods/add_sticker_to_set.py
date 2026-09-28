from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_sticker import InputSticker
    from ..bot import TelegramBot

def add_sticker_to_set(bot: TelegramBot, user_id: int, name: str, sticker_: InputSticker) -> bool:
    """Use this method to add a new sticker to a set created by the bot. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers. Returns True on success."""
    payload = {
        'user_id': user_id,
        'name': name,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('addStickerToSet', payload, files=files if files else None)
