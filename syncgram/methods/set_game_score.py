from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message import Message
    from ..bot import TelegramBot

def set_game_score(bot: TelegramBot, user_id: int, score: int, force: bool | None = None, disable_edit_message: bool | None = None, chat_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None) -> Message | bool:
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""
    payload = {
        'user_id': user_id,
        'score': score,
        'force': force,
        'disable_edit_message': disable_edit_message,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
    }
    return bot.request('setGameScore', payload)
