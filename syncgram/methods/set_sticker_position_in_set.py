from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_sticker_position_in_set(bot: TelegramBot, sticker_: str, position: int) -> bool:
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""
    payload = {
        'position': position,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setStickerPositionInSet', payload, files=files if files else None)
