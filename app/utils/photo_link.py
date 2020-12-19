from io import BytesIO

import aiohttp

from aiogram import types
from aiogram.bot import Bot

from app.loader import telegraph


async def low_photo_link(photo: types.photo_size.PhotoSize) -> str:
    bot = Bot.get_current()
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )
        async with bot.session.post('https://telegra.ph/upload', data=form) as response:
            img_src = await response.json()

    link = 'http://telegra.ph/' + img_src[0]["src"]
    return link


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        links = await telegraph.upload(file)
    return links[0]
