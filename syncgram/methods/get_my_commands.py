from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_command import BotCommand
    from ..objects.bot_command_scope import BotCommandScope
    from ..bot import TelegramBot

def get_my_commands(bot: TelegramBot, scope: BotCommandScope | None = None, language_code: str | None = None) -> list[BotCommand]:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""
    payload = {
        'scope': scope,
        'language_code': language_code,
    }
    return bot.request('getMyCommands', payload)
