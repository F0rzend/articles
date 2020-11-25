from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from app.loader import dp


@dp.message_handler(CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer(f'Hello, {msg.from_user.full_name}!')
