from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def unban_chat_member(bot: TelegramBot, chat_id: str | int, user_id: int, only_if_banned: bool | None = None) -> bool:
    """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'only_if_banned': only_if_banned,
    }
    return bot.request('unbanChatMember', payload)
