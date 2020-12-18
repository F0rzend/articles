import aiohttp
from aiogram import types

from app import config
from app.loader import dp

from os.path import basename


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    file = await msg.photo[-1].download(config.DATA_PATH)
    with open(file.name, 'rb') as f:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=f,
            filename=basename(f.name)
        )
        request_answer = await dp.bot.session.post(
            'https://telegra.ph/upload',
            data=form,
        )

    img_src = await request_answer.json()
    link = 'http://telegra.ph/' + img_src[0]["src"]

    await msg.answer(link)
