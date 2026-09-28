from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_file import InputFile
    from ..bot import TelegramBot

def set_sticker_set_thumbnail(bot: TelegramBot, name: str, user_id: int, format: str, thumbnail: InputFile | str | None = None) -> bool:
    """Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns True on success."""
    payload = {
        'name': name,
        'user_id': user_id,
        'format': format,
        'thumbnail': thumbnail,
    }
    return bot.request('setStickerSetThumbnail', payload)
