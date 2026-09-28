from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.business_connection import BusinessConnection
    from ..bot import TelegramBot

def get_business_connection(bot: TelegramBot, business_connection_id: str) -> BusinessConnection:
    """Use this method to get information about the connection of the bot with a business account. Returns a BusinessConnection object on success."""
    payload = {
        'business_connection_id': business_connection_id,
    }
    return bot.request('getBusinessConnection', payload)
