from typing import List, Union

from loguru import logger

from app.misc import dp


async def notify_admins(admins: Union[List[int], List[str], int, str]):
    count = 0
    for admin in admins:
        await dp.bot.send_message(admin, "Bot started")
        count += 1
    logger.info(f"{count} admins received messages")
