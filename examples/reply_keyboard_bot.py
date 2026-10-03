from syncgram import TelegramBot, EventRouter
from syncgram.objects import ReplyKeyboardMarkup, KeyboardButton
import logging

# Configure logging to show informational messages.
logging.basicConfig(level=logging.INFO)

# Create the bot and register event handlers with a router.
bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()

@router.command("start")
def start_command(message):
    # Create a reply keyboard with two buttons.
    r_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Button_1")],
            [KeyboardButton(text="Button_2")]
        ]
    )

    bot.methods.send_message(message.chat.id, "Choose button:", reply_markup=r_keyboard)

# Handle messages sent when a user presses a reply keyboard button.
@router.message()
def receive_messages(message):
    # Respond according to the button text received.
    if message.text == "Button_1":
        bot.methods.send_message(message.chat.id, "You choosed Button 1!")
    elif message.text == "Button_2":
        bot.methods.send_message(message.chat.id, "You choosed Button 2!")

if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)