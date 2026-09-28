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

def send_video(bot: TelegramBot, chat_id: str | int, video_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, duration: int | None = None, width: int | None = None, height: int | None = None, thumbnail: InputFile | str | None = None, cover: InputFile | str | None = None, start_timestamp: int | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None, supports_streaming: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardRemove | ReplyKeyboardMarkup | InlineKeyboardMarkup | ForceReply | None = None) -> Message:
    """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
    payload = {
        'chat_id': chat_id,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'ephemeral_message_parameters': ephemeral_message_parameters,
        'duration': duration,
        'width': width,
        'height': height,
        'thumbnail': thumbnail,
        'cover': cover,
        'start_timestamp': start_timestamp,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'show_caption_above_media': show_caption_above_media,
        'has_spoiler': has_spoiler,
        'supports_streaming': supports_streaming,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    files = {
        'video': video_,
    }
    files = {k: v for k, v in files.items() if v is not None}
    return bot.request('sendVideo', payload, files=files if files else None)
