from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.story import Story
    from ..bot import TelegramBot

def repost_story(bot: TelegramBot, business_connection_id: str, from_chat_id: int, from_story_id: int, active_period: int, post_to_chat_page: bool | None = None, protect_content: bool | None = None) -> Story:
    """Reposts a story on behalf of a business account from another business account. Both business accounts must be managed by the same bot, and the story on the source account must have been posted (or reposted) by the bot. Requires the can_manage_stories business bot right for both business accounts. Returns Story on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'from_chat_id': from_chat_id,
        'from_story_id': from_story_id,
        'active_period': active_period,
        'post_to_chat_page': post_to_chat_page,
        'protect_content': protect_content,
    }
    return bot.request('repostStory', payload)
