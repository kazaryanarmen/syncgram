from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def send_chat_join_request_web_app(bot: TelegramBot, chat_join_request_query_id: str, web_app_url: str) -> bool:
    """Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome. Call answerChatJoinRequestQuery to resolve the join request query based on the user interaction with the Mini App. Returns True on success."""
    payload = {
        'chat_join_request_query_id': chat_join_request_query_id,
        'web_app_url': web_app_url,
    }
    return bot.request('sendChatJoinRequestWebApp', payload)
