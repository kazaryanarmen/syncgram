from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_custom_emoji_sticker_set_thumbnail(bot: TelegramBot, name: str, custom_emoji_id: str | None = None) -> bool:
    """Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success."""
    payload = {
        'name': name,
        'custom_emoji_id': custom_emoji_id,
    }
    return bot.request('setCustomEmojiStickerSetThumbnail', payload)
