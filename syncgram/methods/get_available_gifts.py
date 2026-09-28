from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.gifts import Gifts
    from ..bot import TelegramBot

def get_available_gifts(bot: TelegramBot) -> Gifts:
    """Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters. Returns a Gifts object."""
    payload = {
    }
    return bot.request('getAvailableGifts', payload)
