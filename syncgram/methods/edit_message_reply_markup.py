from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message import Message
    from ..bot import TelegramBot

def edit_message_reply_markup(bot: TelegramBot, business_connection_id: str | None = None, chat_id: str | int | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
    """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
        'reply_markup': reply_markup,
    }
    return bot.request('editMessageReplyMarkup', payload)
