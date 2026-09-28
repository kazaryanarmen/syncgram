from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def send_chat_action(bot: TelegramBot, chat_id: str | int, action: str, business_connection_id: str | None = None, message_thread_id: int | None = None) -> bool:
    """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success. We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive."""
    payload = {
        'chat_id': chat_id,
        'action': action,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
    }
    return bot.request('sendChatAction', payload)
