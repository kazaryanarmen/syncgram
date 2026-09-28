from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.star_transactions import StarTransactions
    from ..bot import TelegramBot

def get_star_transactions(bot: TelegramBot, offset: int | None = None, limit: int | None = None) -> StarTransactions:
    """Returns the bot's Telegram Star transactions in chronological order. On success, returns a StarTransactions object."""
    payload = {
        'offset': offset,
        'limit': limit,
    }
    return bot.request('getStarTransactions', payload)
