from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_query_result import InlineQueryResult
    from ..objects.prepared_inline_message import PreparedInlineMessage
    from ..bot import TelegramBot

def save_prepared_inline_message(bot: TelegramBot, user_id: int, result: InlineQueryResult, allow_user_chats: bool | None = None, allow_bot_chats: bool | None = None, allow_group_chats: bool | None = None, allow_channel_chats: bool | None = None) -> PreparedInlineMessage:
    """Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object."""
    payload = {
        'user_id': user_id,
        'result': result,
        'allow_user_chats': allow_user_chats,
        'allow_bot_chats': allow_bot_chats,
        'allow_group_chats': allow_group_chats,
        'allow_channel_chats': allow_channel_chats,
    }
    return bot.request('savePreparedInlineMessage', payload)
