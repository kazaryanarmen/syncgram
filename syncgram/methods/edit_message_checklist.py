from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_checklist import InputChecklist
    from ..objects.message import Message
    from ..bot import TelegramBot

def edit_message_checklist(bot: TelegramBot, business_connection_id: str, chat_id: str | int, message_id: int, checklist: InputChecklist, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
    """Use this method to edit a checklist on behalf of a connected business account. On success, the edited Message is returned."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'checklist': checklist,
        'reply_markup': reply_markup,
    }
    return bot.request('editMessageChecklist', payload)
