from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.labeled_price import LabeledPrice
    from ..objects.message import Message
    from ..objects.reply_parameters import ReplyParameters
    from ..objects.suggested_post_parameters import SuggestedPostParameters
    from ..bot import TelegramBot

def send_invoice(bot: TelegramBot, chat_id: str | int, title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
    """Use this method to send invoices. On success, the sent Message is returned."""
    payload = {
        'chat_id': chat_id,
        'title': title,
        'description': description,
        'payload': payload,
        'currency': currency,
        'prices': prices,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'provider_token': provider_token,
        'max_tip_amount': max_tip_amount,
        'suggested_tip_amounts': suggested_tip_amounts,
        'start_parameter': start_parameter,
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
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('sendInvoice', payload)
