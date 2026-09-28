from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_ephemeral_message(bot: TelegramBot, chat_id: str | int, receiver_user_id: int, ephemeral_message_id: int) -> bool:
    """Use this method to delete an ephemeral message. Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'receiver_user_id': receiver_user_id,
        'ephemeral_message_id': ephemeral_message_id,
    }
    return bot.request('deleteEphemeralMessage', payload)
