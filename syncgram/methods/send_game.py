from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message import Message
    from ..objects.reply_parameters import ReplyParameters
    from ..bot import TelegramBot

def send_game(bot: TelegramBot, chat_id: str | int, game_short_name: str, business_connection_id: str | None = None, message_thread_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
    """Use this method to send a game. On success, the sent Message is returned."""
    payload = {
        'chat_id': chat_id,
        'game_short_name': game_short_name,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('sendGame', payload)
