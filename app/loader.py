from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.files import JSONStorage


from app import config

bot = Bot(
    token=config.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)

storage = JSONStorage('storage.json')

dp = Dispatcher(
    bot=bot,
    storage=storage,
)

__all__ = (
    "bot",
    "storage",
    "dp",
)
