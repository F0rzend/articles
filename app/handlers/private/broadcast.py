import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage, BaseStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.utils.broadcast import CopyBroadcast
from app.config import SUPERUSER_IDS  # Список айдишников суперпользователей из конфига


async def broadcast_command_handler(msg: Message, state: FSMContext):
    """
    Обработчик, выполняемый после ввода команды /broadcast
    """
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text')


async def get_users(storage: BaseStorage):
    """
    Функция, возвращающая список айдишников пользователей,
    которые будут получать сообщения в результате рассылки

    Замените её на свою функцию, достающую айди из базы данных
    """
    if isinstance(storage, MemoryStorage):
        users = list(storage.data.keys())  # Если в качестве storage используется ОЗУ, достаём айдишники из неё
    else:
        users = SUPERUSER_IDS  # В противном случае рассылку делаем по админам
        logging.warning('Рассылка по суперпользователям')
    return users


async def start_broadcast(msg: Message, state: FSMContext):
    """
        Обработчик, начинающий рассылку с введённым пользователем текстом
        """
    await state.finish()
    storage = state.storage
    users = await get_users(storage)  # Список айдишников, можете доставать из базы данных или как вам удобнее.
    await CopyBroadcast(users, msg).run()
