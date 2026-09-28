from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_user_emoji_status(bot: TelegramBot, user_id: int, emoji_status_custom_emoji_id: str | None = None, emoji_status_expiration_date: int | None = None) -> bool:
    """Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success."""
    payload = {
        'user_id': user_id,
        'emoji_status_custom_emoji_id': emoji_status_custom_emoji_id,
        'emoji_status_expiration_date': emoji_status_expiration_date,
    }
    return bot.request('setUserEmojiStatus', payload)
