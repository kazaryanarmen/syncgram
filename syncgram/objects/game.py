from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .animation import Animation
    from .message_entity import MessageEntity
    from .photo_size import PhotoSize

class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers."""
    def __init__(self, title: str, description: str, photo_: list[PhotoSize], text: str | None = None, text_entities: list[MessageEntity] | None = None, animation_: Animation | None = None):
        self.title: str = title
        self.description: str = description
        self.photo_: list[PhotoSize] = photo_
        self.text: str | None = text
        self.text_entities: list[MessageEntity] | None = text_entities
        self.animation_: Animation | None = animation_

    def to_dict(self) -> dict:
        def _serialize(v):
            if hasattr(v, 'to_dict'):
                return v.to_dict()
            elif isinstance(v, list):
                return [_serialize(i) for i in v]
            elif isinstance(v, dict):
                return {k: _serialize(val) for k, val in v.items()}
            return v
        result = {}
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.text_entities is not None:
            result['text_entities'] = _serialize(self.text_entities)
        if self.animation_ is not None:
            result['animation'] = _serialize(self.animation_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Game' | None:
        if not data:
            return None
        from .animation import Animation
        from .message_entity import MessageEntity
        from .photo_size import PhotoSize
        photo__raw = data.get('photo')
        photo_ = [PhotoSize.from_dict(i) for i in photo__raw] if photo__raw else None
        text_entities_raw = data.get('text_entities')
        text_entities = [MessageEntity.from_dict(i) for i in text_entities_raw] if text_entities_raw else None
        return cls(
            title=data.get('title'),
            description=data.get('description'),
            photo_=photo_,
            text=data.get('text'),
            text_entities=text_entities,
            animation_=Animation.from_dict(data.get('animation')),
        )
