from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def edit_ephemeral_message_caption(bot: TelegramBot, chat_id: str | int, receiver_user_id: int, ephemeral_message_id: int, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
    """Use this method to edit the caption of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
    payload = {
        'chat_id': chat_id,
        'receiver_user_id': receiver_user_id,
        'ephemeral_message_id': ephemeral_message_id,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'show_caption_above_media': show_caption_above_media,
        'reply_markup': reply_markup,
    }
    return bot.request('editEphemeralMessageCaption', payload)
