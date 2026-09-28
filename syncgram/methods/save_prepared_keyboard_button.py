from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.keyboard_button import KeyboardButton
    from ..objects.prepared_keyboard_button import PreparedKeyboardButton
    from ..bot import TelegramBot

def save_prepared_keyboard_button(bot: TelegramBot, user_id: int, button: KeyboardButton) -> PreparedKeyboardButton:
    """Stores a keyboard button that can be used by a user within a Mini App. Returns a PreparedKeyboardButton object."""
    payload = {
        'user_id': user_id,
        'button': button,
    }
    return bot.request('savePreparedKeyboardButton', payload)
