from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def set_chat_member_tag(bot: TelegramBot, chat_id: str | int, user_id: int, tag: str | None = None) -> bool:
    """Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the can_manage_tags administrator right. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'tag': tag,
    }
    return bot.request('setChatMemberTag', payload)
