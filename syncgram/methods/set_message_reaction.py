from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.reaction_type import ReactionType
    from ..bot import TelegramBot

def set_message_reaction(bot: TelegramBot, chat_id: str | int, message_id: int, reaction: list[ReactionType] | None = None, is_big: bool | None = None) -> bool:
    """Use this method to change the chosen reactions on a message. Service messages of some types can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can't use paid reactions. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': reaction,
        'is_big': is_big,
    }
    return bot.request('setMessageReaction', payload)
