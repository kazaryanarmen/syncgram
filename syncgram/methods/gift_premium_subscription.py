from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def gift_premium_subscription(bot: TelegramBot, user_id: int, month_count: int, star_count: int, text: str | None = None, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None) -> bool:
    """Gifts a Telegram Premium subscription to the given user. Returns True on success."""
    payload = {
        'user_id': user_id,
        'month_count': month_count,
        'star_count': star_count,
        'text': text,
        'text_parse_mode': text_parse_mode,
        'text_entities': text_entities,
    }
    return bot.request('giftPremiumSubscription', payload)
