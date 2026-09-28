from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_media import InputMedia
    from ..objects.message import Message
    from ..bot import TelegramBot

def edit_message_media(bot: TelegramBot, media: InputMedia, business_connection_id: str | None = None, chat_id: str | int | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
    """Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
    payload = {
        'media': media,
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
        'reply_markup': reply_markup,
    }
    return bot.request('editMessageMedia', payload)
