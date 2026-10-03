from syncgram import TelegramBot, EventRouter
from syncgram.objects import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("start")
def start_command(message):
    # Attach a callback button to the message that will be edited.
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Edit message", callback_data="edit_message")]
        ]
    )

    bot.methods.send_message(
        chat_id=message.chat.id,
        text="Press the button to edit this message.",
        reply_markup=keyboard,
    )


@router.callback_query()
def edit_message(query):
    if query.data != "edit_message" or query.message is None:
        return

    bot.methods.answer_callback_query(
        callback_query_id=query.id,
        text="Message updated.",
    )
    bot.methods.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="This message has been edited.",
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)