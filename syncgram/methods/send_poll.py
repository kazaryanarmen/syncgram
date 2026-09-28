from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.force_reply import ForceReply
    from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
    from ..objects.input_poll_media import InputPollMedia
    from ..objects.input_poll_option import InputPollOption
    from ..objects.message import Message
    from ..objects.message_entity import MessageEntity
    from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup
    from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
    from ..objects.reply_parameters import ReplyParameters
    from ..bot import TelegramBot

def send_poll(bot: TelegramBot, chat_id: str | int, question: str, options: list[InputPollOption], business_connection_id: str | None = None, message_thread_id: int | None = None, question_parse_mode: str | None = None, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | None = None, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMedia | None = None, open_period: int | None = None, close_date: int | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | None = None, description_entities: list[MessageEntity] | None = None, media: InputPollMedia | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardRemove | ReplyKeyboardMarkup | InlineKeyboardMarkup | ForceReply | None = None) -> Message:
    """Use this method to send a native poll. On success, the sent Message is returned."""
    payload = {
        'chat_id': chat_id,
        'question': question,
        'options': options,
        'business_connection_id': business_connection_id,
        'message_thread_id': message_thread_id,
        'question_parse_mode': question_parse_mode,
        'question_entities': question_entities,
        'is_anonymous': is_anonymous,
        'type': type,
        'allows_multiple_answers': allows_multiple_answers,
        'allows_revoting': allows_revoting,
        'shuffle_options': shuffle_options,
        'allow_adding_options': allow_adding_options,
        'hide_results_until_closes': hide_results_until_closes,
        'members_only': members_only,
        'country_codes': country_codes,
        'correct_option_ids': correct_option_ids,
        'explanation': explanation,
        'explanation_parse_mode': explanation_parse_mode,
        'explanation_entities': explanation_entities,
        'explanation_media': explanation_media,
        'open_period': open_period,
        'close_date': close_date,
        'is_closed': is_closed,
        'description': description,
        'description_parse_mode': description_parse_mode,
        'description_entities': description_entities,
        'media': media,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'allow_paid_broadcast': allow_paid_broadcast,
        'message_effect_id': message_effect_id,
        'reply_parameters': reply_parameters,
        'reply_markup': reply_markup,
    }
    return bot.request('sendPoll', payload)
