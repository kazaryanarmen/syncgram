from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..bot import TelegramBot

def edit_ephemeral_message_reply_markup(bot: TelegramBot, chat_id: str | int, receiver_user_id: int, ephemeral_message_id: int, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
    """Use this method to edit only the reply markup of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
    payload = {
        'chat_id': chat_id,
        'receiver_user_id': receiver_user_id,
        'ephemeral_message_id': ephemeral_message_id,
        'reply_markup': reply_markup,
    }
    return bot.request('editEphemeralMessageReplyMarkup', payload)
