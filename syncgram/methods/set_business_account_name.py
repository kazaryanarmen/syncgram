from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_business_account_name(bot: TelegramBot, business_connection_id: str, first_name: str, last_name: str | None = None) -> bool:
    """Changes the first and last name of a managed business account. Requires the can_change_name business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'first_name': first_name,
        'last_name': last_name,
    }
    return bot.request('setBusinessAccountName', payload)
