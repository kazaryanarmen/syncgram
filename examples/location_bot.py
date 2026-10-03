from syncgram import TelegramBot, EventRouter
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("location")
def send_location(message):
    # Send the coordinates of central London as an example location.
    bot.methods.send_location(
        chat_id=message.chat.id,
        latitude=51.5074,
        longitude=-0.1278,
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)