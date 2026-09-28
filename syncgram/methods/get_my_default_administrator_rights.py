from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_administrator_rights import ChatAdministratorRights
    from ..bot import TelegramBot

def get_my_default_administrator_rights(bot: TelegramBot, for_channels: bool | None = None) -> ChatAdministratorRights:
    """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
    payload = {
        'for_channels': for_channels,
    }
    return bot.request('getMyDefaultAdministratorRights', payload)
