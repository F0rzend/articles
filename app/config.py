from pathlib import Path

from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
SKIP_UPDATES = env.bool("SKIP_UPDATES", False)
WORK_PATH: Path = Path(__file__).parent.parent

SUPERUSER_IDS = env.list("SUPERUSER_IDS")
