from syncgram import TelegramBot, EventRouter

# Initialize the bot
bot = TelegramBot(token="BOT_TOKEN")

# Initialize the router
router = EventRouter()

# Register a message handler
@router.message()
def receive_messages(message):
    bot.methods.send_message(
        chat_id=message.chat.id,
        text=f"You said: {message.text}"
    )

# Start the bot via polling
if __name__ == "__main__":
    bot.start_polling(router)
    