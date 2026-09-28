from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.shipping_option import ShippingOption
    from ..bot import TelegramBot

def answer_shipping_query(bot: TelegramBot, shipping_query_id: str, ok: bool, shipping_options: list[ShippingOption] | None = None, error_message: str | None = None) -> bool:
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""
    payload = {
        'shipping_query_id': shipping_query_id,
        'ok': ok,
        'shipping_options': shipping_options,
        'error_message': error_message,
    }
    return bot.request('answerShippingQuery', payload)
