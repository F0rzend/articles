from aiogram.utils import exceptions
import logging

from .errors.retry_after import retry_after_error
from .private.start import command_start_handler
from .private.broadcast import broadcast_command_handler, start_broadcast

from aiogram import Dispatcher, filters, types


def setup(dp: Dispatcher):
    dp.register_errors_handler(retry_after_error, exception=exceptions.RetryAfter)
    dp.register_message_handler(command_start_handler, filters.CommandStart())

    dp.register_message_handler(broadcast_command_handler, commands='broadcast')
    dp.register_message_handler(start_broadcast, state='broadcast_text', content_types=types.ContentTypes.ANY)

    logging.info("Handlers are successfully configured")
