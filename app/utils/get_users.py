import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Dispatcher

from app.config import SUPERUSER_IDS  # Список айдишников суперпользователей из конфига


async def get_users():
    """
    Функция, возвращающая список айдишников пользователей,
    которые будут получать сообщения в результате рассылки

    Замените её на свою функцию, достающую айди из базы данных
    """
    dp = Dispatcher.get_current()
    storage = dp.storage
    if isinstance(storage, MemoryStorage):
        users = list(storage.data.keys())  # Если в качестве storage используется ОЗУ, достаём айдишники из неё
    else:
        users = SUPERUSER_IDS  # В противном случае рассылку делаем по админам
        logging.warning('Рассылка по суперпользователям')
    return users
