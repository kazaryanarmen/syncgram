from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_query_result import InlineQueryResult
    from ..objects.sent_guest_message import SentGuestMessage
    from ..bot import TelegramBot

def answer_guest_query(bot: TelegramBot, guest_query_id: str, result: InlineQueryResult) -> SentGuestMessage:
    """Use this method to reply to a received guest message. On success, a SentGuestMessage object is returned."""
    payload = {
        'guest_query_id': guest_query_id,
        'result': result,
    }
    return bot.request('answerGuestQuery', payload)
