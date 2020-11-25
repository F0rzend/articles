from aiogram.utils import exceptions
from loguru import logger

from app.loader import dp


@dp.errors_handler(exception=exceptions.RetryAfter)
async def retry_after_error(update, exception):
    logger.exception(f'RetryAfter: {exception} \nUpdate: {update}')
    return True
