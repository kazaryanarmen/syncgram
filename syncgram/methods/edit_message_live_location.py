from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message import Message
    from ..bot import TelegramBot

def edit_message_live_location(bot: TelegramBot, latitude: float, longitude: float, business_connection_id: str | None = None, chat_id: str | int | None = None, message_id: int | None = None, inline_message_id: str | None = None, live_period: int | None = None, horizontal_accuracy: float | None = None, heading: int | None = None, proximity_alert_radius: int | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
        'live_period': live_period,
        'horizontal_accuracy': horizontal_accuracy,
        'heading': heading,
        'proximity_alert_radius': proximity_alert_radius,
        'reply_markup': reply_markup,
    }
    return bot.request('editMessageLiveLocation', payload)
