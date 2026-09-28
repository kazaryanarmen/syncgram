from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def ban_chat_member(bot: TelegramBot, chat_id: str | int, user_id: int, until_date: int | None = None, revoke_messages: bool | None = None) -> bool:
    """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': until_date,
        'revoke_messages': revoke_messages,
    }
    return bot.request('banChatMember', payload)
