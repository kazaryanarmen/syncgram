from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_invite_link import ChatInviteLink
    from ..bot import TelegramBot

def edit_chat_subscription_invite_link(bot: TelegramBot, chat_id: str | int, invite_link: str, name: str | None = None) -> ChatInviteLink:
    """Use this method to edit a subscription invite link created by the bot. The bot must have the can_invite_users administrator rights. Returns the edited invite link as a ChatInviteLink object."""
    payload = {
        'chat_id': chat_id,
        'invite_link': invite_link,
        'name': name,
    }
    return bot.request('editChatSubscriptionInviteLink', payload)
