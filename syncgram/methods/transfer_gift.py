from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def transfer_gift(bot: TelegramBot, business_connection_id: str, owned_gift_id: str, new_owner_chat_id: int, star_count: int | None = None) -> bool:
    """Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right. Requires can_transfer_stars business bot right if the transfer is paid. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'owned_gift_id': owned_gift_id,
        'new_owner_chat_id': new_owner_chat_id,
        'star_count': star_count,
    }
    return bot.request('transferGift', payload)
