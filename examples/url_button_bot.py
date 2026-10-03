from syncgram import TelegramBot, EventRouter
from syncgram.objects import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("start")
def start_command(message):
    # URL buttons open the specified pages directly.
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Telegram Bot API", url="https://core.telegram.org/bots/api")],
            [InlineKeyboardButton(text="Syncgram on GitHub", url="https://github.com/kazaryanarmen/syncgram")],
        ]
    )

    bot.methods.send_message(
        chat_id=message.chat.id,
        text="Choose a link:",
        reply_markup=keyboard,
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)