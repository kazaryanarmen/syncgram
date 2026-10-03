from syncgram import TelegramBot, EventRouter
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("contact")
def send_sample_contact(message):
    # Replace this sample number with the contact details you intend to share.
    bot.methods.send_contact(
        chat_id=message.chat.id,
        phone_number="+1234567890",
        first_name="Example Contact",
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)