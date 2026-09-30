# Syncgram

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyPI version](https://img.shields.io/pypi/v/syncgram.svg)](https://pypi.org/project/syncgram/)
[![Telegram Bot API](https://img.shields.io/badge/Bot%20API-10.3-blue?logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)


**Syncgram** is a simple, lightweight, and synchronous Python library for creating Telegram bots. No `async/await` boilerplate—just clean, straightforward code and convenient routing using routers.

---

## 🚀 Installation

**Github:**

```bash
pip install git+https://github.com/kazaryanarmen/syncgram.git
```

**Python:**

```bash
pip install syncgram
```

💡 **Quick Start**

Create a simple echo bot in just a few minutes:

```python
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
```

✨ **Features**

Synchronous Approach: Perfect for small scripts, automation tools, and developers who prefer blocking code over async loops.

• Easy Routing: Cleanly organize your bot's logic using EventRouter.

• Simple API: Minimal abstraction layers for a fast and frictionless start.

🛠️ **Contributing**

Contributions, issues, and feature requests are welcome! Feel free to check out the issues page or submit a Pull Request.

📄 **License**

This project is distributed under the MIT License.

[**Subscribe SyncGram Dev**](https://t.me/syncgramdev)
