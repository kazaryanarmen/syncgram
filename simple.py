from syncgram import TelegramBot

# init bot
bot = TelegramBot(token="8615494848:AAF0H1pON7f5EN1EdhSm-y7Ek3FAuK2gqqg")

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