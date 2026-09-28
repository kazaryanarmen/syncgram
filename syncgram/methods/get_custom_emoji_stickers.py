from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.sticker import Sticker
    from ..bot import TelegramBot

def get_custom_emoji_stickers(bot: TelegramBot, custom_emoji_ids: list[str]) -> list[Sticker]:
    """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects."""
    payload = {
        'custom_emoji_ids': custom_emoji_ids,
    }
    return bot.request('getCustomEmojiStickers', payload)
