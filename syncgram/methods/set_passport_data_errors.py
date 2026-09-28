from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.passport_element_error import PassportElementError
    from ..bot import TelegramBot

def set_passport_data_errors(bot: TelegramBot, user_id: int, errors: list[PassportElementError]) -> bool:
    """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success. Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues."""
    payload = {
        'user_id': user_id,
        'errors': errors,
    }
    return bot.request('setPassportDataErrors', payload)
