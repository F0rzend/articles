import aiohttp
from aiogram import types

from app.loader import dp

from tempfile import NamedTemporaryFile


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    with NamedTemporaryFile(mode='wb', prefix='file_', suffix='.jpg') as file:
        await photo.download(file.name)
        with open(file.name, 'rb') as f:
            form = aiohttp.FormData()
            form.add_field(
                name='file',
                value=f,
            )
            request_answer = await dp.bot.session.post(
                'https://telegra.ph/upload',
                data=form,
            )

    img_src = await request_answer.json()
    link = 'http://telegra.ph/' + img_src[0]["src"]

    await msg.answer(link)
