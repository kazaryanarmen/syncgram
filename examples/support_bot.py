from syncgram import TelegramBot, EventRouter
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()

# Replace these placeholders with the support chat ID and an authorized admin's user ID.
ADMIN_CHAT_ID = -1001234567890
ADMIN_USER_ID = 123456789


@router.command("start")
def start_command(message):
    bot.methods.send_message(
        chat_id=message.chat.id,
        text="Send a message here and it will be forwarded to support.",
    )


@router.command("reply")
def reply_to_user(message):
    # Only the configured admin can reply to users from the support chat.
    if (
        message.chat.id != ADMIN_CHAT_ID
        or message.from_ is None
        or message.from_.id != ADMIN_USER_ID
    ):
        return

    parts = (message.text or "").split(maxsplit=2)
    if len(parts) != 3:
        bot.methods.send_message(
            chat_id=ADMIN_CHAT_ID,
            text="Usage: /reply <user_chat_id> <message>",
        )
        return

    try:
        user_chat_id = int(parts[1])
    except ValueError:
        bot.methods.send_message(
            chat_id=ADMIN_CHAT_ID,
            text="The user chat ID must be a number.",
        )
        return

    bot.methods.send_message(chat_id=user_chat_id, text=parts[2])


@router.message()
def forward_to_support(message):
    # Do not forward messages sent by admins in the configured support chat.
    if message.chat.id == ADMIN_CHAT_ID:
        return
    if message.text is not None and message.text.startswith("/"):
        return

    bot.methods.forward_message(
        chat_id=ADMIN_CHAT_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
    )
    bot.methods.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"Reply with /reply {message.chat.id} <message>",
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)