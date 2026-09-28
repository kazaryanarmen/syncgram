from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import TelegramBot

def promote_chat_member(bot: TelegramBot, chat_id: str | int, user_id: int, is_anonymous: bool | None = None, can_manage_chat: bool | None = None, can_delete_messages: bool | None = None, can_manage_video_chats: bool | None = None, can_restrict_members: bool | None = None, can_promote_members: bool | None = None, can_change_info: bool | None = None, can_invite_users: bool | None = None, can_post_stories: bool | None = None, can_edit_stories: bool | None = None, can_delete_stories: bool | None = None, can_post_messages: bool | None = None, can_edit_messages: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, can_manage_direct_messages: bool | None = None, can_manage_tags: bool | None = None, can_send_welcome_messages: bool | None = None) -> bool:
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
    payload = {
        'chat_id': chat_id,
        'user_id': user_id,
        'is_anonymous': is_anonymous,
        'can_manage_chat': can_manage_chat,
        'can_delete_messages': can_delete_messages,
        'can_manage_video_chats': can_manage_video_chats,
        'can_restrict_members': can_restrict_members,
        'can_promote_members': can_promote_members,
        'can_change_info': can_change_info,
        'can_invite_users': can_invite_users,
        'can_post_stories': can_post_stories,
        'can_edit_stories': can_edit_stories,
        'can_delete_stories': can_delete_stories,
        'can_post_messages': can_post_messages,
        'can_edit_messages': can_edit_messages,
        'can_pin_messages': can_pin_messages,
        'can_manage_topics': can_manage_topics,
        'can_manage_direct_messages': can_manage_direct_messages,
        'can_manage_tags': can_manage_tags,
        'can_send_welcome_messages': can_send_welcome_messages,
    }
    return bot.request('promoteChatMember', payload)
