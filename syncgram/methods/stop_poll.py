from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.poll import Poll
    from ..bot import TelegramBot

def stop_poll(bot: TelegramBot, chat_id: str | int, message_id: int, business_connection_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Poll:
    """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'business_connection_id': business_connection_id,
        'reply_markup': reply_markup,
    }
    return bot.request('stopPoll', payload)
