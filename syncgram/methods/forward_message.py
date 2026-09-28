from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message import Message
    from ..objects.suggested_post_parameters import SuggestedPostParameters
    from ..bot import TelegramBot

def forward_message(bot: TelegramBot, chat_id: str | int, from_chat_id: str | int, message_id: int, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, video_start_timestamp: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None) -> Message:
    """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent Message is returned."""
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'video_start_timestamp': video_start_timestamp,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
    }
    return bot.request('forwardMessage', payload)
