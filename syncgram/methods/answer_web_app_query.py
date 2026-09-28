from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_query_result import InlineQueryResult
    from ..objects.sent_web_app_message import SentWebAppMessage
    from ..bot import TelegramBot

def answer_web_app_query(bot: TelegramBot, web_app_query_id: str, result: InlineQueryResult) -> SentWebAppMessage:
    """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""
    payload = {
        'web_app_query_id': web_app_query_id,
        'result': result,
    }
    return bot.request('answerWebAppQuery', payload)
