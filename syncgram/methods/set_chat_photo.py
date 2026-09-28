from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_file import InputFile
    from ..bot import TelegramBot

def set_chat_photo(bot: TelegramBot, chat_id: str | int, photo_: InputFile) -> bool:
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    files = {
        'photo': photo_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('setChatPhoto', payload, files=files if files else None)
