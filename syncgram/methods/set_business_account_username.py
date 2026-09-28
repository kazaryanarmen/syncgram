from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_business_account_username(bot: TelegramBot, business_connection_id: str, username: str | None = None) -> bool:
    """Changes the username of a managed business account. Requires the can_change_username business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'username': username,
    }
    return bot.request('setBusinessAccountUsername', payload)
