from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.star_amount import StarAmount
    from ..bot import TelegramBot

def get_my_star_balance(bot: TelegramBot) -> StarAmount:
    """A method to get the current Telegram Stars balance of the bot. Requires no parameters. On success, returns a StarAmount object."""
    payload = {
    }
    return bot.request('getMyStarBalance', payload)
