from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chat import Chat
    from .message import Message

class MaybeInaccessibleMessage:
    """This object describes a message that can be inaccessible to the bot."""
    def __init__(self, chat: Chat | None = None, message_id: int | None = None, date: int | None = None, **kwargs):
        self.chat: Chat | None = chat
        self.message_id: int | None = message_id
        self.date: int | None = date
        for k, v in kwargs.items():
            setattr(self, k, v)

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
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
            
        for k, v in self.__dict__.items():
            if k not in ('chat', 'message_id', 'date') and v is not None:
                result[k] = _serialize(v)
                
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MaybeInaccessibleMessage' | Message | None:
        if not data:
            return None
            
        from .chat import Chat
        from .message import Message  

        if 'text' in data or 'photo' in data or 'document' in data or 'from' in data or 'audio' in data:
            return Message.from_dict(data)
            
        chat = Chat.from_dict(data.get('chat')) if data.get('chat') else None
        
        return cls(
            chat=chat,
            message_id=data.get('message_id'),
            date=data.get('date')
        )