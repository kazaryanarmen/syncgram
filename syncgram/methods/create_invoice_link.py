from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.labeled_price import LabeledPrice
    from ..bot import TelegramBot

def create_invoice_link(bot: TelegramBot, title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], business_connection_id: str | None = None, provider_token: str | None = None, subscription_period: int | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None) -> str:
    """Use this method to create a link for an invoice. Returns the created invoice link as String on success."""
    payload = {
        'title': title,
        'description': description,
        'payload': payload,
        'currency': currency,
        'prices': prices,
        'business_connection_id': business_connection_id,
        'provider_token': provider_token,
        'subscription_period': subscription_period,
        'max_tip_amount': max_tip_amount,
        'suggested_tip_amounts': suggested_tip_amounts,
        'provider_data': provider_data,
        'photo_url': photo_url,
        'photo_size': photo_size,
        'photo_width': photo_width,
        'photo_height': photo_height,
        'need_name': need_name,
        'need_phone_number': need_phone_number,
        'need_email': need_email,
        'need_shipping_address': need_shipping_address,
        'send_phone_number_to_provider': send_phone_number_to_provider,
        'send_email_to_provider': send_email_to_provider,
        'is_flexible': is_flexible,
    }
    return bot.request('createInvoiceLink', payload)
