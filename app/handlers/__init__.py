from loguru import logger

from .errors import retry_after
from .private import start, telegraph

logger.info("Handlers are successfully configured")
