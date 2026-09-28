from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_permissions import ChatPermissions
    from ..bot import TelegramBot

def restrict_chat_member(bot: TelegramBot, chat_id: str | int, user_id: int, permissions: ChatPermissions, use_independent_chat_permissions: bool | None = None, until_date: int | None = None) -> bool:
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'permissions': permissions,
        'use_independent_chat_permissions': use_independent_chat_permissions,
        'until_date': until_date,
    }
    return bot.request('restrictChatMember', payload)
