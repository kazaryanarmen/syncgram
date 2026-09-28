from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_story_content import InputStoryContent
    from ..objects.message_entity import MessageEntity
    from ..objects.story import Story
    from ..objects.story_area import StoryArea
    from ..bot import TelegramBot

def post_story(bot: TelegramBot, business_connection_id: str, content: InputStoryContent, active_period: int, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, areas: list[StoryArea] | None = None, post_to_chat_page: bool | None = None, protect_content: bool | None = None) -> Story:
    """Posts a story on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns Story on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'content': content,
        'active_period': active_period,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'areas': areas,
        'post_to_chat_page': post_to_chat_page,
        'protect_content': protect_content,
    }
    return bot.request('postStory', payload)
