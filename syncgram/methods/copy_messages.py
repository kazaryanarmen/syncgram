from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.message_id import MessageId
    from ..bot import TelegramBot

def copy_messages(bot: TelegramBot, chat_id: str | int, from_chat_id: str | int, message_ids: list[int], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, remove_caption: bool | None = None) -> list[MessageId]:
    """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_ids is known to the bot. The method is analogous to the method forwardMessages, but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an Array of MessageId of the sent messages is returned."""
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_ids': message_ids,
        'message_thread_id': message_thread_id,
        'direct_messages_topic_id': direct_messages_topic_id,
        'disable_notification': disable_notification,
        'protect_content': protect_content,
        'remove_caption': remove_caption,
    }
    return bot.request('copyMessages', payload)
