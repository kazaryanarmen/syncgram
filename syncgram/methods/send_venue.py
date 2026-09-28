from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.ephemeral_message_parameters import EphemeralMessageParameters
    from ..objects.force_reply import ForceReply
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message import Message
    from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup
    from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
    from ..objects.reply_parameters import ReplyParameters
    from ..objects.suggested_post_parameters import SuggestedPostParameters
    from ..bot import TelegramBot

def send_venue(bot: TelegramBot, chat_id: str | int, latitude: float, longitude: float, title: str, address: str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardRemove | ReplyKeyboardMarkup | InlineKeyboardMarkup | ForceReply | None = None) -> Message:
    """Use this method to send information about a venue. On success, the sent Message is returned."""
    payload = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'title': title,
        'address': address,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'ephemeral_message_parameters': ephemeral_message_parameters,
        'foursquare_id': foursquare_id,
        'foursquare_type': foursquare_type,
        'google_place_id': google_place_id,
        'google_place_type': google_place_type,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('sendVenue', payload)
