Keyboards
=========

In **SyncGram**, you can easily create both standard text keyboards (Reply) and inline buttons attached to messages (Inline).

Reply Keyboards
---------------

Reply keyboards replace the user's standard device keyboard. Here is an example of creating a simple keyboard with action buttons:

.. code-block:: python

   from syncgram import TelegramBot, EventRouter
   from syncgram.types import ReplyKeyboardMarkup, KeyboardButton

   # Initialize the bot and router
   bot = TelegramBot(token="BOT_TOKEN")
   router = EventRouter()

   @router.command("start")
   def send_welcome(message):
       # Create a Reply keyboard
       keyboard = ReplyKeyboardMarkup(
           keyboard=[
               [KeyboardButton(text="Hello 👋"), KeyboardButton(text="Help ℹ️")]
           ],
           resize_keyboard=True
       )
       bot.methods.send_message(
           chat_id=message.chat.id,
           text="Choose an action:",
           reply_markup=keyboard
       )

   if __name__ == "__main__":
       bot.start_polling(router)

Inline Keyboards
----------------

Inline keyboards are attached directly to the message. They are perfect for interactive menus and links:

.. code-block:: python

   from syncgram import TelegramBot, EventRouter
   from syncgram.types import InlineKeyboardMarkup, InlineKeyboardButton

   # Initialize the bot and router
   bot = TelegramBot(token="BOT_TOKEN")
   router = EventRouter()

   @router.command("menu")
   def send_menu(message):
       # Create an Inline keyboard
       keyboard = InlineKeyboardMarkup(
           inline_keyboard=[
               [InlineKeyboardButton(text="Open Website", url="https://python.org")],
               [InlineKeyboardButton(text="Click Me", callback_data="btn_click")]
           ]
       )
       bot.methods.send_message(
           chat_id=message.chat.id,
           text="Interactive menu:",
           reply_markup=keyboard
       )

   if __name__ == "__main__":
       bot.start_polling(router)