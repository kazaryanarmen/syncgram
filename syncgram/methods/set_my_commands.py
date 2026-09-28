from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_command import BotCommand
    from ..objects.bot_command_scope import BotCommandScope
    from ..bot import TelegramBot

def set_my_commands(bot: TelegramBot, commands: list[BotCommand], scope: BotCommandScope | None = None, language_code: str | None = None) -> bool:
    """Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success."""
    payload = {
        'commands': commands,
        'scope': scope,
        'language_code': language_code,
    }
    return bot.request('setMyCommands', payload)
