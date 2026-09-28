from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.input_file import InputFile
    from ..bot import TelegramBot

def set_webhook(bot: TelegramBot, url: str, certificate: InputFile | None = None, ip_address: str | None = None, max_connections: int | None = None, allowed_updates: list[str] | None = None, drop_pending_updates: bool | None = None, secret_token: str | None = None) -> bool:
    """Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request (a request with response HTTP status code different from 2XY), we will repeat the request and give up after a reasonable amount of attempts. Returns True on success. If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content."""
    payload = {
        'url': url,
        'certificate': certificate,
        'ip_address': ip_address,
        'max_connections': max_connections,
        'allowed_updates': allowed_updates,
        'drop_pending_updates': drop_pending_updates,
        'secret_token': secret_token,
    }
    return bot.request('setWebhook', payload)
