from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_chat_sticker_set(bot: TelegramBot, chat_id: str | int) -> bool:
    """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('deleteChatStickerSet', payload)
