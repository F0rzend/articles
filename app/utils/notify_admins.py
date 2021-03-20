from .broadcast import types, TextBroadcast


async def notify_admins(admins: types.ChatsType):
    await TextBroadcast(admins, '$chat_id, The bot is running!').run()
