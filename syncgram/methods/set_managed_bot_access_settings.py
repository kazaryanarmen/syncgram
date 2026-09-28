from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_managed_bot_access_settings(bot: TelegramBot, user_id: int, is_access_restricted: bool, added_user_ids: list[int] | None = None) -> bool:
    """Use this method to change the access settings of a managed bot. Returns True on success."""
    payload = {
        'user_id': user_id,
        'is_access_restricted': is_access_restricted,
        'added_user_ids': added_user_ids,
    }
    return bot.request('setManagedBotAccessSettings', payload)
