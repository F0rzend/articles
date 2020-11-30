from typing import List, Union
from contextlib import suppress
from aiogram.utils.exceptions import ChatNotFound

from loguru import logger

from app.loader import dp


async def notify_admins(admins: Union[List[int], List[str], int, str]):
    count = 0
    for admin in admins:
        with suppress(ChatNotFound):
            await dp.bot.send_message(admin, "Bot started")
            count += 1
    logger.info(f"{count} admins received messages")
