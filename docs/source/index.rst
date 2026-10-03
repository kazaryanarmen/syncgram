Welcome to SyncGram Documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   api

**SyncGram** is a convenient Python library for creating Telegram bots.

Quick Start
-----------

Install the library via pip:

.. code-block:: bash

   pip install syncgram

Example of a simple bot:

.. code-block:: python

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

Reference
---------

* :doc:`api` — Complete API reference for classes and methods.