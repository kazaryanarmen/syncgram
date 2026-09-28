from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def refund_star_payment(bot: TelegramBot, user_id: int, telegram_payment_charge_id: str) -> bool:
    """Refunds a successful payment in Telegram Stars. Returns True on success."""
    payload = {
        'user_id': user_id,
        'telegram_payment_charge_id': telegram_payment_charge_id,
    }
    return bot.request('refundStarPayment', payload)
