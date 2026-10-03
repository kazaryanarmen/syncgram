from syncgram import TelegramBot, EventRouter
from syncgram.objects import InputPollOption
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("poll")
def send_sample_poll(message):
    # Poll options are represented by InputPollOption objects.
    bot.methods.send_poll(
        chat_id=message.chat.id,
        question="Which feature should we build next?",
        options=[
            InputPollOption(text="More examples"),
            InputPollOption(text="More documentation"),
            InputPollOption(text="Both"),
        ],
        allows_multiple_answers=True,
    )


if __name__ == "__main__":
    # Start polling Telegram for updates and dispatch them through the router.
    bot.start_polling(router)