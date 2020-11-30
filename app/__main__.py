from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, config
from app.loader import dp

# The configuration of the modules using import
from app import middlewares, filters, handlers


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(config.SUPERUSER_IDS)


if __name__ == '__main__':
    utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    executor.start_polling(
        dp, on_startup=on_startup, skip_updates=config.SKIP_UPDATES
    )
