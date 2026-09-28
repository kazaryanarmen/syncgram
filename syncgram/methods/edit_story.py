from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_story_content import InputStoryContent
    from ..objects.message_entity import MessageEntity
    from ..objects.story import Story
    from ..objects.story_area import StoryArea
    from ..bot import TelegramBot

def edit_story(bot: TelegramBot, business_connection_id: str, story_id: int, content: InputStoryContent, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, areas: list[StoryArea] | None = None) -> Story:
    """Edits a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns Story on success."""
    payload = {
        'business_connection_id': business_connection_id,
        'story_id': story_id,
        'content': content,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'areas': areas,
    }
    return bot.request('editStory', payload)
