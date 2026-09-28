from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.file import File
    from ..objects.input_file import InputFile
    from ..bot import TelegramBot

def upload_sticker_file(bot: TelegramBot, user_id: int, sticker_: InputFile, sticker_format: str) -> File:
    """Use this method to upload a file with a sticker for later use in the createNewStickerSet, addStickerToSet, or replaceStickerInSet methods (the file can be used multiple times). Returns the uploaded File on success."""
    payload = {
        'user_id': user_id,
        'sticker_format': sticker_format,
    }
    files = {
        'sticker': sticker_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('uploadStickerFile', payload, files=files if files else None)
