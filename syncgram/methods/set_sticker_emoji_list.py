from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_sticker_emoji_list(bot: TelegramBot, sticker_: str, emoji_list: list[str]) -> bool:
    """Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
    payload = {
        'emoji_list': emoji_list,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setStickerEmojiList', payload, files=files if files else None)
