from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def send_message_draft(bot: TelegramBot, chat_id: int, draft_id: int, message_thread_id: int | None = None, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, can_stop: bool | None = None, keep_on_stop: bool | None = None) -> bool:
    """Use this method to stream a partial message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you must call sendMessage with the complete message to persist it in the user's chat. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'draft_id': draft_id,
        'message_thread_id': message_thread_id,
        'text': text,
        'parse_mode': parse_mode,
        'entities': entities,
        'can_stop': can_stop,
        'keep_on_stop': keep_on_stop,
    }
    return bot.request('sendMessageDraft', payload)
