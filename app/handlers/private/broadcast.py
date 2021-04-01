from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from aiogram_broadcaster import MessageBroadcaster
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
    users = await get_users()  # Список айдишников, можете доставать из базы данных или как вам удобнее.
    await MessageBroadcaster(users, msg).run()
