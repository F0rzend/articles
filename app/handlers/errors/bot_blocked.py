from aiogram import types
from aiogram.utils import exceptions
from loguru import logger

from app.loader import dp


@dp.errors_handler(exception=exceptions.BotBlocked)
async def bot_blocked_error(update: types.Update, exception: exceptions.BotBlocked):
    logger.exception(f'Bot blocked by user {update.message.from_user.id}')
    return True
