from aiogram_broadcaster import types, TextBroadcaster


async def notify_admins(admins: types.ChatsType):
    await TextBroadcaster(admins, '$chat_id, The bot is running!').run()
