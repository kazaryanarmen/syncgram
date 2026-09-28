from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def delete_story(bot: TelegramBot, business_connection_id: str, story_id: int) -> bool:
    """Deletes a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns True on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'story_id': story_id,
    }
    return bot.request('deleteStory', payload)
