from contextlib import suppress

from gino import UninitializedError

from loguru import logger

from app.misc import db


async def connect(postgres_uri):
    await db.set_bind(postgres_uri)
    logger.info('PostgreSQL is successfully configured')


async def close_connection():
    with suppress(UninitializedError):
        logger.info('Closing a database connection')
        await db.pop_bind().close()
