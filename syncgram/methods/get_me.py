from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.user import User
    from ..bot import TelegramBot

def get_me(bot: TelegramBot) -> User:
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
    payload = {
    }
    return bot.request('getMe', payload)
