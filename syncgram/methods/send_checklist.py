from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_checklist import InputChecklist
    from ..objects.message import Message
    from ..objects.reply_parameters import ReplyParameters
    from ..bot import TelegramBot

def send_checklist(bot: TelegramBot, business_connection_id: str, chat_id: str | int, checklist: InputChecklist, disable_notification: bool | None = None, protect_content: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
    """Use this method to send a checklist on behalf of a connected business account. On success, the sent Message is returned."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'checklist': checklist,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'message_effect_id': message_effect_id,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('sendChecklist', payload)
