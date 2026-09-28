from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def decline_chat_join_request(bot: TelegramBot, chat_id: str | int, user_id: int) -> bool:
    """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
    }
    return bot.request('declineChatJoinRequest', payload)
