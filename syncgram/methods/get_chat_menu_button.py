from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.menu_button import MenuButton
    from ..bot import TelegramBot

def get_chat_menu_button(bot: TelegramBot, chat_id: int | None = None) -> MenuButton:
    """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('getChatMenuButton', payload)
