from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.force_reply import ForceReply
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.message_entity import MessageEntity
    from ..objects.message_id import MessageId
    from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup
    from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
    from ..objects.reply_parameters import ReplyParameters
    from ..objects.suggested_post_parameters import SuggestedPostParameters
    from ..bot import TelegramBot

def copy_message(bot: TelegramBot, chat_id: str | int, from_chat_id: str | int, message_id: int, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, video_start_timestamp: int | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardRemove | ReplyKeyboardMarkup | InlineKeyboardMarkup | ForceReply | None = None) -> MessageId:
    """Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_ids is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'video_start_timestamp': video_start_timestamp,
        'caption': caption,
        'parse_mode': parse_mode,
        'caption_entities': caption_entities,
        'show_caption_above_media': show_caption_above_media,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'suggested_post_parameters': suggested_post_parameters,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('copyMessage', payload)
