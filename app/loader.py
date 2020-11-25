from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from app import config

bot = Bot(
    token=config.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)

storage = MemoryStorage()

dp = Dispatcher(
    bot=bot,
    storage=storage,
)

__all__ = (
    "bot",
    "storage",
    "dp",
)
