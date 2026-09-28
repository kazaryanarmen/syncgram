from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_permissions import ChatPermissions
    from ..bot import TelegramBot

def set_chat_permissions(bot: TelegramBot, chat_id: str | int, permissions: ChatPermissions, use_independent_chat_permissions: bool | None = None) -> bool:
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'permissions': permissions,
        'use_independent_chat_permissions': use_independent_chat_permissions,
    }
    return bot.request('setChatPermissions', payload)
