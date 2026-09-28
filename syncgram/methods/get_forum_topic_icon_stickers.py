from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.sticker import Sticker
    from ..bot import TelegramBot

def get_forum_topic_icon_stickers(bot: TelegramBot) -> list[Sticker]:
    """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects."""
    payload = {
    }
    return bot.request('getForumTopicIconStickers', payload)
