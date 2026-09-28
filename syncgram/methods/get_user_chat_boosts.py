from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.user_chat_boosts import UserChatBoosts
    from ..bot import TelegramBot

def get_user_chat_boosts(bot: TelegramBot, chat_id: str | int, user_id: int) -> UserChatBoosts:
    """Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
    }
    return bot.request('getUserChatBoosts', payload)
