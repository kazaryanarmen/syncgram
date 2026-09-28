from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.game_high_score import GameHighScore
    from ..bot import TelegramBot

def get_game_high_scores(bot: TelegramBot, user_id: int, chat_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None) -> list[GameHighScore]:
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects."""
    payload = {
        'user_id': user_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
    }
    return bot.request('getGameHighScores', payload)
