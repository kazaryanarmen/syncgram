from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.ephemeral_message_parameters import EphemeralMessageParameters
    from ..objects.force_reply import ForceReply
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_file import InputFile
    from ..objects.message import Message
    from ..objects.message_entity import MessageEntity
    from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup
    from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
    from ..objects.reply_parameters import ReplyParameters
    from ..objects.suggested_post_parameters import SuggestedPostParameters
    from ..bot import TelegramBot

def send_audio(bot: TelegramBot, chat_id: str | int, audio_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, duration: int | None = None, performer: str | None = None, title: str | None = None, thumbnail: InputFile | str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardRemove | ReplyKeyboardMarkup | InlineKeyboardMarkup | ForceReply | None = None) -> Message:
    """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future. For sending voice messages, use the sendVoice method instead."""
    payload = {
        'chat_id': chat_id,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'ephemeral_message_parameters': ephemeral_message_parameters,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'duration': duration,
        'performer': performer,
        'title': title,
        'thumbnail': thumbnail,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    files = {
        'audio': audio_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('sendAudio', payload, files=files if files else None)
