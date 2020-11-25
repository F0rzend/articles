from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from app.loader import dp

if __name__ == "app.middlewares":
    dp.middleware.setup(LoggingMiddleware())
    logger.info('Middlewares are successfully configured')
