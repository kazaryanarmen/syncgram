from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_query_result import InlineQueryResult
    from ..objects.inline_query_results_button import InlineQueryResultsButton
    from ..bot import TelegramBot

def answer_inline_query(bot: TelegramBot, inline_query_id: str, results: list[InlineQueryResult], cache_time: int | None = None, is_personal: bool | None = None, next_offset: str | None = None, button: InlineQueryResultsButton | None = None) -> bool:
    """Use this method to send answers to an inline query. On success, True is returned. No more than 50 results per query are allowed."""
    payload = {
        'inline_query_id': inline_query_id,
        'results': results,
        'cache_time': cache_time,
        'is_personal': is_personal,
        'next_offset': next_offset,
        'button': button,
    }
    return bot.request('answerInlineQuery', payload)
