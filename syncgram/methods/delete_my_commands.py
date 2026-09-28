from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.bot_command_scope import BotCommandScope
    from ..bot import TelegramBot

def delete_my_commands(bot: TelegramBot, scope: BotCommandScope | None = None, language_code: str | None = None) -> bool:
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
    payload = {
        'scope': scope,
        'language_code': language_code,
    }
    return bot.request('deleteMyCommands', payload)
