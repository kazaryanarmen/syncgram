from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.menu_button import MenuButton
    from ..bot import TelegramBot

def set_chat_menu_button(bot: TelegramBot, chat_id: int | None = None, menu_button: MenuButton | None = None) -> bool:
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'menu_button': menu_button,
    }
    return bot.request('setChatMenuButton', payload)
