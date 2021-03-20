from loguru import logger

from aiogram import Dispatcher


def setup(dp: Dispatcher):
    logger.info('Filters are successfully configured')
