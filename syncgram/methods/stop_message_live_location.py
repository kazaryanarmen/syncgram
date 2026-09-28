from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message import Message
    from ..bot import TelegramBot

def stop_message_live_location(bot: TelegramBot, business_connection_id: str | None = None, chat_id: str | int | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
    """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
        'reply_markup': reply_markup,
    }
    return bot.request('stopMessageLiveLocation', payload)
