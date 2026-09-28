from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_invite_link import ChatInviteLink
    from ..bot import TelegramBot

def revoke_chat_invite_link(bot: TelegramBot, chat_id: str | int, invite_link: str) -> ChatInviteLink:
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
    payload = {
        'chat_id': chat_id,
        'invite_link': invite_link,
    }
    return bot.request('revokeChatInviteLink', payload)
