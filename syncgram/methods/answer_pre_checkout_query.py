from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def answer_pre_checkout_query(bot: TelegramBot, pre_checkout_query_id: str, ok: bool, error_message: str | None = None) -> bool:
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent."""
    payload = {
        'pre_checkout_query_id': pre_checkout_query_id,
        'ok': ok,
        'error_message': error_message,
    }
    return bot.request('answerPreCheckoutQuery', payload)
