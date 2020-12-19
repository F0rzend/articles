from aiogram import types

from app.loader import dp
from app.utils import photo_link, photo_link_


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]

    await msg.bot.send_chat_action(msg.chat.id, 'upload_photo')
    link = await photo_link(photo)
    await msg.answer(link)

    await msg.bot.send_chat_action(msg.chat.id, 'upload_photo')
    link = await photo_link_(photo)
    await msg.answer(link)
