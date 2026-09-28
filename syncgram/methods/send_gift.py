from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def send_gift(bot: TelegramBot, gift_id: str, user_id: int | None = None, chat_id: str | int | None = None, pay_for_upgrade: bool | None = None, text: str | None = None, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None) -> bool:
    """Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns True on success."""
    payload = {
        'gift_id': gift_id,
        'user_id': user_id,
        'chat_id': chat_id,
        'pay_for_upgrade': pay_for_upgrade,
        'text': text,
        'text_parse_mode': text_parse_mode,
        'text_entities': text_entities,
    }
    return bot.request('sendGift', payload)
