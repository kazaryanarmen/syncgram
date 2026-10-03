from syncgram import TelegramBot, EventRouter
from syncgram.objects import InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Configure logging to show informational messages.
logging.basicConfig(level=logging.INFO)

# Create the bot and register event handlers with a router.
bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()

@router.command("start")
def start_command(message):
    # Build an inline keyboard with callback data for each button.
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Button_1", callback_data="btn_1")],
            [InlineKeyboardButton(text="Button_2", callback_data="btn_2")]
        ]
    )

    bot.methods.send_message(
        message.chat.id, 
        "Choose button:", 
        reply_markup=keyboard
    )

# Handle button presses sent as callback queries.
@router.callback_query()
def handle_buttons(query):
    # Acknowledge the pressed button and send a matching message.
    if query.data == "btn_1":
        bot.methods.answer_callback_query(query.id, text="You pressed Button 1!")
        bot.methods.send_message(
            query.message.chat.id,
            text="You choosed Button 1!"
        )

    elif query.data == "btn_2":
        bot.methods.answer_callback_query(query.id, text="You pressed Button 2!")
        bot.methods.send_message(
            query.message.chat.id,
            text="You choosed Button 2!"
        )

if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)