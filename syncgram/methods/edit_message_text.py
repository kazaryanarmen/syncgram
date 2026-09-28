from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_rich_message import InputRichMessage
    from ..objects.link_preview_options import LinkPreviewOptions
    from ..objects.message import Message
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def edit_message_text(bot: TelegramBot, business_connection_id: str | None = None, chat_id: str | int | None = None, message_id: int | None = None, inline_message_id: str | None = None, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, link_preview_options: LinkPreviewOptions | None = None, rich_message: InputRichMessage | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
    """Use this method to edit text, rich and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
    payload = {
        'business_connection_id': business_connection_id,
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_message_id': inline_message_id,
        'text': text,
        'parse_mode': parse_mode,
        'entities': entities,
        'link_preview_options': link_preview_options,
        'rich_message': rich_message,
        'reply_markup': reply_markup,
    }
    return bot.request('editMessageText', payload)
