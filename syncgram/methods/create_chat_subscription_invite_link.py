from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_invite_link import ChatInviteLink
    from ..bot import TelegramBot

def create_chat_subscription_invite_link(bot: TelegramBot, chat_id: str | int, subscription_period: int, subscription_price: int, name: str | None = None) -> ChatInviteLink:
    """Use this method to create a subscription invite link for a channel chat. The bot must have the can_invite_users administrator rights. The link can be edited using the method editChatSubscriptionInviteLink or revoked using the method revokeChatInviteLink. Returns the new invite link as a ChatInviteLink object."""
    payload = {
        'chat_id': chat_id,
        'subscription_period': subscription_period,
        'subscription_price': subscription_price,
        'name': name,
    }
    return bot.request('createChatSubscriptionInviteLink', payload)
