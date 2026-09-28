from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_media_audio import InputMediaAudio
    from ..objects.input_media_document import InputMediaDocument
    from ..objects.input_media_live_photo import InputMediaLivePhoto
    from ..objects.input_media_photo import InputMediaPhoto
    from ..objects.input_media_video import InputMediaVideo
    from ..objects.message import Message
    from ..objects.reply_parameters import ReplyParameters
    from ..bot import TelegramBot

def send_media_group(bot: TelegramBot, chat_id: str | int, media: list[InputMediaLivePhoto] | list[InputMediaVideo] | list[InputMediaAudio] | list[InputMediaDocument] | list[InputMediaPhoto], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None) -> list[Message]:
    """Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of Message objects that were sent is returned."""
    payload = {
        'chat_id': chat_id,
        'media': media,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'reply_parameters': reply_parameters,
    }
    return bot.request('sendMediaGroup', payload)
