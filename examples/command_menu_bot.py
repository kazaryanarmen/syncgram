from syncgram import TelegramBot, EventRouter
from syncgram.objects import BotCommand
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")
router = EventRouter()


@router.command("start")
def start_command(message):
    bot.methods.send_message(
        chat_id=message.chat.id,
        text="Welcome! Use /help to see the available commands.",
    )


@router.command("help")
def help_command(message):
    bot.methods.send_message(
        chat_id=message.chat.id,
        text="Available commands: /start and /help",
    )


if __name__ == "__main__":
    # Register commands so Telegram can show them in the bot's command menu.
    bot.methods.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start the bot"),
            BotCommand(command="help", description="Show available commands"),
        ]
    )
    bot.start_polling(router)