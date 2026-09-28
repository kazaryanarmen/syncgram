from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.accepted_gift_types import AcceptedGiftTypes
    from ..bot import TelegramBot

def set_business_account_gift_settings(bot: TelegramBot, business_connection_id: str, show_gift_button: bool, accepted_gift_types: AcceptedGiftTypes) -> bool:
    """Changes the privacy settings pertaining to incoming gifts in a managed business account. Requires the can_change_gift_settings business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'show_gift_button': show_gift_button,
        'accepted_gift_types': accepted_gift_types,
    }
    return bot.request('setBusinessAccountGiftSettings', payload)
