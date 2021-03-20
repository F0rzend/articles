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


async def start_broadcast(msg: Message, state: FSMContext):
    """
    Обработчик, начинающий рассылку с введённым пользователем текстом
    """
    await state.finish()
    users = SUPERUSER_IDS * 20  # Список айдишников, можете доставать из базы данных или как вам удобнее.
    # Я буду просто отправлять себе 20 сообщений для примера
    await CopyBroadcast(users, msg).run()
