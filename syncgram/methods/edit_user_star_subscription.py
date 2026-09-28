from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def edit_user_star_subscription(bot: TelegramBot, user_id: int, telegram_payment_charge_id: str, is_canceled: bool) -> bool:
    """Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns True on success."""
    payload = {
        'user_id': user_id,
        'telegram_payment_charge_id': telegram_payment_charge_id,
        'is_canceled': is_canceled,
    }
    return bot.request('editUserStarSubscription', payload)
