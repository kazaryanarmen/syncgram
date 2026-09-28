from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def answer_chat_join_request_query(bot: TelegramBot, chat_join_request_query_id: str, result: str) -> bool:
    """Use this method to process a received chat join request query. Returns True on success."""
    payload = {
        'chat_join_request_query_id': chat_join_request_query_id,
        'result': result,
    }
    return bot.request('answerChatJoinRequestQuery', payload)
