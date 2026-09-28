from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_sticker_set_title(bot: TelegramBot, name: str, title: str) -> bool:
    """Use this method to set the title of a created sticker set. Returns True on success."""
    payload = {
        'name': name,
        'title': title,
    }
    return bot.request('setStickerSetTitle', payload)
