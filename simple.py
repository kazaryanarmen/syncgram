from syncgram import TelegramBot

# init bot
bot = TelegramBot(token="BOT-TOKEN")

# import EventRouter
from syncgram import EventRouter

# init router
router = EventRouter()

# create routers
@router.message()
def receive_messages(message):
    bot.methods.send_message(chat_id=message.chat.id,
                             text=f"You said: {message.text}")

# start bot
if __name__ == "__main__":
    bot.start_polling(router)
