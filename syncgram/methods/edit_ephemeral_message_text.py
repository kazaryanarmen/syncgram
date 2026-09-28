from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_rich_message import InputRichMessage
    from ..objects.link_preview_options import LinkPreviewOptions
    from ..objects.message_entity import MessageEntity
    from ..bot import TelegramBot

def edit_ephemeral_message_text(bot: TelegramBot, chat_id: str | int, receiver_user_id: int, ephemeral_message_id: int, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, rich_message: InputRichMessage | None = None, link_preview_options: LinkPreviewOptions | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
    """Use this method to edit an ephemeral text or rich message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
    payload = {
        'chat_id': chat_id,
        'receiver_user_id': receiver_user_id,
        'ephemeral_message_id': ephemeral_message_id,
        'text': text,
        'parse_mode': parse_mode,
        'entities': entities,
        'rich_message': rich_message,
        'link_preview_options': link_preview_options,
        'reply_markup': reply_markup,
    }
    return bot.request('editEphemeralMessageText', payload)
