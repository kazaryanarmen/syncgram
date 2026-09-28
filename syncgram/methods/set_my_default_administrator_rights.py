from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.chat_administrator_rights import ChatAdministratorRights
    from ..bot import TelegramBot

def set_my_default_administrator_rights(bot: TelegramBot, rights: ChatAdministratorRights | None = None, for_channels: bool | None = None) -> bool:
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success."""
    payload = {
        'rights': rights,
        'for_channels': for_channels,
    }
    return bot.request('setMyDefaultAdministratorRights', payload)
