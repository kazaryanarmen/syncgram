import requests
import json
import time
from .exceptions import TelegramBadRequestError, TelegramUnauthorizedError, TelegramNetworkError, TelegramAPIError
from .methods.get_updates import get_updates
from .methods import __all__ as all_methods

class MethodsProxy:
    def __init__(self, bot: 'TelegramBot'):
        self._bot = bot
        from . import methods
        for method_name in all_methods:
            method_func = getattr(methods, method_name)
            setattr(self, method_name, lambda *args, func=method_func, **kwargs: func(self._bot, *args, **kwargs))

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.file_url = f"https://api.telegram.org/file/bot{token}"
        self.session = requests.Session()
        self.methods = MethodsProxy(self)

    def request(self, method_name: str, params: dict | None = None, files: dict | None = None) -> dict:
        url = f"{self.base_url}/{method_name}"
        if params:
            cleaned_params = {}
            for k, v in params.items():
                if v is not None:
                    if hasattr(v, 'to_dict'):
                        v = v.to_dict()
                    elif isinstance(v, list):
                        v = [i.to_dict() if hasattr(i, 'to_dict') else i for i in v]

                    if isinstance(v, (dict, list)):
                        v = json.dumps(v)

                    original_key = k[:-1] if k.endswith('_') and k[:-1] in ['from', 'photo', 'video', 'document', 'audio', 'sticker', 'animation', 'voice'] else k
                    cleaned_params[original_key] = v
            params = cleaned_params
        
        try:
            response = self.session.post(url, data=params, files=files, timeout=60)
        except requests.RequestException as e:
            raise TelegramNetworkError(f"Network error during request to {method_name}: {e}")

        try:
            data = response.json()
        except ValueError:
            raise TelegramAPIError("Received an invalid JSON response from the Telegram server.")

        if not data.get("ok", False):
            error_code = data.get("error_code")
            description = data.get("description", "Unknown error")
            
            if error_code == 401:
                raise TelegramUnauthorizedError(f"Authorization error: {description}", error_code)
            elif error_code == 400:
                raise TelegramBadRequestError(f"Bad request: {description}", error_code)
            else:
                raise TelegramAPIError(f"API error [{error_code}]: {description}", error_code)

        return data.get("result")

    def download_file(self, file_path: str, destination_path: str) -> None:
        url = f"{self.file_url}/{file_path}"
        try:
            response = self.session.get(url, stream=True, timeout=60)
            if response.status_code == 200:
                with open(destination_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                raise TelegramAPIError(f"Failed to download file. Status code: {response.status_code}")
        except requests.RequestException as e:
            raise TelegramNetworkError(f"Network error while downloading file: {e}")

    def start_polling(self, router, interval: float = 1.0) -> None:
        offset = 0

        bot_username = "Unknown Bot"

        try:
            me = self.methods.get_me()

            if isinstance(me, dict) and "username" in me:
                bot_username = f"@{me['username']}"
            elif hasattr(me, "username") and me.username:
                bot_username = f"@{me.username}"
        except Exception:
            pass
    
        print("\n" + "=" * 45)
        print(f"🤖 Bot {bot_username} is up and running!")
        print("📡 Polling for updates... (Press Ctrl+C to stop)")
        print("=" * 45 + "\n")
    
        while True:
            try:
                updates = self.methods.get_updates(offset=offset, timeout=30)
                
                if updates:
                    for update in updates:
                        if isinstance(update, dict):
                            offset = update.get("update_id", offset) + 1
                            router.feed(update)
                        else:
                            offset = getattr(update, "update_id", offset) + 1
                            if hasattr(update, 'to_dict'):
                                router.feed(update.to_dict())
                            else:
                                router.feed(update)
            except KeyboardInterrupt:
                print("\n" + "=" * 45)
                print(f"🛑 Polling for {bot_username} stopped gracefully. Goodbye!")
                print("=" * 45)
                break
            except Exception as e:
                print(f"⚠️ Polling error: {e}")
        
            time.sleep(interval)
