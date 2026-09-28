from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def export_chat_invite_link(bot: TelegramBot, chat_id: str | int) -> str:
    """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
    payload = {
        'chat_id': chat_id,
    }
    return bot.request('exportChatInviteLink', payload)
