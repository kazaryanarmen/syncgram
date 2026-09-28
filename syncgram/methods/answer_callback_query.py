from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def answer_callback_query(bot: TelegramBot, callback_query_id: str, text: str | None = None, show_alert: bool | None = None, url: str | None = None, cache_time: int | None = None) -> bool:
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
    payload = {
        'callback_query_id': callback_query_id,
        'text': text,
        'show_alert': show_alert,
        'url': url,
        'cache_time': cache_time,
    }
    return bot.request('answerCallbackQuery', payload)
