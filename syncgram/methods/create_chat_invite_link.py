from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_invite_link import ChatInviteLink
    from ..bot import TelegramBot

def create_chat_invite_link(bot: TelegramBot, chat_id: str | int, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, creates_join_request: bool | None = None) -> ChatInviteLink:
    """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
    payload = {
        'chat_id': chat_id,
        'name': name,
        'expire_date': expire_date,
        'member_limit': member_limit,
        'creates_join_request': creates_join_request,
    }
    return bot.request('createChatInviteLink', payload)
