from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.utils.broadcast import CopyBroadcast
from app.utils.get_users import get_users


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
    storage = state.storage
    users = await get_users(storage)  # Список айдишников, можете доставать из базы данных или как вам удобнее.
    await CopyBroadcast(users, msg).run()
