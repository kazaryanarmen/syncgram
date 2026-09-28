from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_sticker_keywords(bot: TelegramBot, sticker_: str, keywords: list[str] | None = None) -> bool:
    """Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
    payload = {
        'keywords': keywords,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setStickerKeywords', payload, files=files if files else None)
