from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message_id import MessageId
    from ..bot import TelegramBot

def forward_messages(bot: TelegramBot, chat_id: str | int, from_chat_id: str | int, message_ids: list[int], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None) -> list[MessageId]:
    """Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an Array of MessageId of the sent messages is returned."""
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_ids': message_ids,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
    }
    return bot.request('forwardMessages', payload)
