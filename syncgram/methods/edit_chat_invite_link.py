from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_invite_link import ChatInviteLink
    from ..bot import TelegramBot

def edit_chat_invite_link(bot: TelegramBot, chat_id: str | int, invite_link: str, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, creates_join_request: bool | None = None) -> ChatInviteLink:
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
    payload = {
        'chat_id': chat_id,
        'invite_link': invite_link,
        'name': name,
        'expire_date': expire_date,
        'member_limit': member_limit,
        'creates_join_request': creates_join_request,
    }
    return bot.request('editChatInviteLink', payload)
