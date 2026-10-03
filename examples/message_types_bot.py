from syncgram import TelegramBot, EventRouter
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.message()
def handle_message(message):
    # Check the message fields to identify the received content type.
    if message.text is not None:
        response = f"You sent a text message: {message.text}"
    elif message.photo_:
        response = "You sent a photo."
    elif message.document_:
        response = "You sent a document."
    elif message.video_:
        response = "You sent a video."
    elif message.voice_:
        response = "You sent a voice message."
    else:
        response = "You sent another type of message."

    bot.methods.send_message(chat_id=message.chat.id, text=response)


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)