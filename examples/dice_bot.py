from syncgram import TelegramBot, EventRouter
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("dice")
def roll_dice(message):
    # Telegram returns an animated die with a random result.
    bot.methods.send_dice(chat_id=message.chat.id)


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)