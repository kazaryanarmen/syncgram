from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def upgrade_gift(bot: TelegramBot, business_connection_id: str, owned_gift_id: str, keep_original_details: bool | None = None, star_count: int | None = None) -> bool:
    """Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right. Additionally requires the can_transfer_stars business bot right if the upgrade is paid. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'owned_gift_id': owned_gift_id,
        'keep_original_details': keep_original_details,
        'star_count': star_count,
    }
    return bot.request('upgradeGift', payload)
