from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.loader import dp
from app.config import SUPERUSER_IDS

IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'
COMMAND_IMAGE_REGEXP = r"/image:" + IMAGE_REGEXP

FORBIDDEN_PHRASE = [
    'Курс',
    'Фигня'
]


@dp.message_handler(chat_type=types.ChatType.PRIVATE, commands='is_pm')
@dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='is_pm')
async def chat_type_example(msg: types.Message):
    await msg.answer('Да, это личные сообщения')


@dp.message_handler(is_forwarded=True)
@dp.message_handler(filters.ForwardedMessageFilter(True))
async def forwarded_example(msg: types.Message):
    await msg.answer('Не пытайся меня обмануть, я же вижу, что это не твоё сообщение')


@dp.message_handler(content_types='contact', is_sender_contact=True)
@dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_example(msg: types.Message):
    await msg.answer('Да, вроде на тебя похож, ладно')


@dp.message_handler(is_reply=True, commands='user_id')
@dp.message_handler(filters.IsReplyFilter(True), commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


@dp.message_handler(commands='change_photo', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def chat_admin_example(msg: types.Message):
    await msg.answer('Не, мне и эта нравится')


@dp.message_handler(filters.Text(contains=FORBIDDEN_PHRASE, ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Сам фигня!')


@dp.message_handler(commands='set_state')
async def set_state(msg: types.Message, state: FSMContext):
    """Присваиваем пользователю состояние для теста"""
    await state.set_state('example_state')
    await msg.answer('Состояние установлено')


@dp.message_handler(state='example_state')
async def state_example(msg: types.Message, state: FSMContext):
    await msg.answer('Ой всё, иди отсюда')
    await state.finish()


@dp.message_handler(filters.RegexpCommandsFilter([COMMAND_IMAGE_REGEXP]))
@dp.message_handler(regexp_commands=[COMMAND_IMAGE_REGEXP])
async def command_regexp_example(msg: types.Message):
    await msg.answer('По вашей команде докладываю, что данная ссылка является изображением!')


@dp.message_handler(filters.Regexp(IMAGE_REGEXP))
@dp.message_handler(regexp=IMAGE_REGEXP)
async def regexp_example(msg: types.Message):
    await msg.answer('Похоже на картинку, не так ли?')


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg: types.Message):
    await msg.answer('Ееее, деньги 😎')


@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(msg: types.Message):
    await msg.answer('Красивенько 😍')


@dp.message_handler(commands='myCommand', commands_ignore_caption=False)
@dp.message_handler(filters.Command('myCommand', ignore_caption=False))
async def command_example(msg: types.Message):
    await msg.answer('Твоя команда, твоя, не кричи')


@dp.message_handler(filters.CommandStart(deep_link='deep_link'))
async def deep_link(msg: types.Message):
    await msg.answer('Да, знаем мы такое')


@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer(f'Ну привет, хотел чего?')


@dp.message_handler(filters.IDFilter(chat_id=SUPERUSER_IDS))
@dp.message_handler(chat_id=SUPERUSER_IDS)
async def id_filter_example(msg: types.Message):
    await msg.answer('Да, помню тебя, наш человек')
