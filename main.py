from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tg_bot = '5272139369:AAEmG3uNSRE3RpVMxsD4KGhEguF01ch7-lo'

bot = Bot(token=tg_bot)
dp = Dispatcher(bot)
rick_sanchez = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/rick_sanchez.jpeg', 'rb')
morty_smith = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/morty_smith.jpeg', 'rb')
summer_smith = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/summer_smith.jpeg', 'rb')
jerry_smith = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/jerry_smith.jpeg', 'rb')
squanchy = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/squanchy.jpeg', 'rb')
beth_smith = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/beth_smith.jpeg', 'rb')
krombopulos_michael = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/krombopulos_michael.jpeg', 'rb')
reverse_giraffe = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/reverse_giraffe.jpeg', 'rb')
birdperson = open('/Users/nuraim/Desktop/my_projects/month_1/telegabot/birdperson.jpeg', 'rb')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Здравствуйте какого персонажа хотите видеть? /Rick_Sanchez '
                        '/Morty_Smith /Summer_Smith /Jerry_Smith /Squanchy /Beth_Smith /Krombopulos_Michael /Reverse_Giraffe /Birdperson')

@dp.message_handler(commands=['Rick_Sanchez'])
async def rick_sanchez_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, rick_sanchez.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='0')
    inl_btn = InlineKeyboardButton('status', callback_data='1')
    inl_btn1 = InlineKeyboardButton('species', callback_data='2')
    inl_btn2 = InlineKeyboardButton('location', callback_data='3')
    inl_btn3 = InlineKeyboardButton('type', callback_data='4')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='5')

    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '0')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Rick Sanchez')

@dp.callback_query_handler(lambda c: c.data == '1')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '2')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Human')

@dp.callback_query_handler(lambda c: c.data == '3')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Citadel of Ricks')

@dp.callback_query_handler(lambda c: c.data == '4')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'no type')

@dp.callback_query_handler(lambda c: c.data == '5')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

####################

@dp.message_handler(commands=['Morty_Smith'])
async def morty_smith_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, morty_smith.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='6')
    inl_btn = InlineKeyboardButton('status', callback_data='7')
    inl_btn1 = InlineKeyboardButton('species', callback_data='8')
    inl_btn2 = InlineKeyboardButton('location', callback_data='9')
    inl_btn3 = InlineKeyboardButton('type', callback_data='10')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='11')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '6')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Morty Smith')

@dp.callback_query_handler(lambda c: c.data == '7')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '8')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Human')

@dp.callback_query_handler(lambda c: c.data == '9')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Citadel of Ricks')

@dp.callback_query_handler(lambda c: c.data == '10')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'no type')

@dp.callback_query_handler(lambda c: c.data == '11')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

######################

@dp.message_handler(commands=['Summer_Smith'])
async def summer_smith_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, summer_smith.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='12')
    inl_btn = InlineKeyboardButton('status', callback_data='13')
    inl_btn1 = InlineKeyboardButton('species', callback_data='14')
    inl_btn2 = InlineKeyboardButton('location', callback_data='15')
    inl_btn3 = InlineKeyboardButton('type', callback_data='16')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='17')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '12')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Summer Smith')

@dp.callback_query_handler(lambda c: c.data == '13')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '14')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Human')

@dp.callback_query_handler(lambda c: c.data == '15')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Earth, Replacement Dimension')

@dp.callback_query_handler(lambda c: c.data == '16')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'no type')

@dp.callback_query_handler(lambda c: c.data == '17')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Female')

#####################

@dp.message_handler(commands=['Jerry_Smith'])
async def jerry_smith_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, jerry_smith.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='18')
    inl_btn = InlineKeyboardButton('status', callback_data='19')
    inl_btn1 = InlineKeyboardButton('species', callback_data='20')
    inl_btn2 = InlineKeyboardButton('location', callback_data='21')
    inl_btn3 = InlineKeyboardButton('type', callback_data='22')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='23')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '18')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Jerry Smith')

@dp.callback_query_handler(lambda c: c.data == '19')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '20')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Human')

@dp.callback_query_handler(lambda c: c.data == '21')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Earth, Replacement Dimension')

@dp.callback_query_handler(lambda c: c.data == '22')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'no type')

@dp.callback_query_handler(lambda c: c.data == '23')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

############################

@dp.message_handler(commands=['squanchy'])
async def squanchy_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, squanchy.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='24')
    inl_btn = InlineKeyboardButton('status', callback_data='25')
    inl_btn1 = InlineKeyboardButton('species', callback_data='26')
    inl_btn2 = InlineKeyboardButton('location', callback_data='27')
    inl_btn3 = InlineKeyboardButton('type', callback_data='28')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='29')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '24')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Squanchy')

@dp.callback_query_handler(lambda c: c.data == '25')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'unknown')

@dp.callback_query_handler(lambda c: c.data == '26')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alien')

@dp.callback_query_handler(lambda c: c.data == '27')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Planet Squanch')

@dp.callback_query_handler(lambda c: c.data == '28')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Cat-Person')

@dp.callback_query_handler(lambda c: c.data == '29')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

######################

@dp.message_handler(commands=['beth_smith'])
async def beth_smith_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, beth_smith.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='30')
    inl_btn = InlineKeyboardButton('status', callback_data='31')
    inl_btn1 = InlineKeyboardButton('species', callback_data='32')
    inl_btn2 = InlineKeyboardButton('location', callback_data='33')
    inl_btn3 = InlineKeyboardButton('type', callback_data='34')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='35')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '30')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Beth Smith')

@dp.callback_query_handler(lambda c: c.data == '31')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '32')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Human')

@dp.callback_query_handler(lambda c: c.data == '33')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Earth, Replacement Dimension')

@dp.callback_query_handler(lambda c: c.data == '34')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'no type')

@dp.callback_query_handler(lambda c: c.data == '35')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Female')

####################

@dp.message_handler(commands=['krombopulos_michael'])
async def krombopulos_michael_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, krombopulos_michael.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='36')
    inl_btn = InlineKeyboardButton('status', callback_data='37')
    inl_btn1 = InlineKeyboardButton('species', callback_data='38')
    inl_btn2 = InlineKeyboardButton('location', callback_data='39')
    inl_btn3 = InlineKeyboardButton('type', callback_data='40')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='41')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '36')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Krombopulos Michael')

@dp.callback_query_handler(lambda c: c.data == '37')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Dead')

@dp.callback_query_handler(lambda c: c.data == '38')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alien')

@dp.callback_query_handler(lambda c: c.data == '39')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'unknown')

@dp.callback_query_handler(lambda c: c.data == '40')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Gromflomite')

@dp.callback_query_handler(lambda c: c.data == '41')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')


####################

@dp.message_handler(commands=['reverse_giraffe'])
async def reverse_giraffe_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, reverse_giraffe.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='42')
    inl_btn = InlineKeyboardButton('status', callback_data='43')
    inl_btn1 = InlineKeyboardButton('species', callback_data='44')
    inl_btn2 = InlineKeyboardButton('location', callback_data='45')
    inl_btn3 = InlineKeyboardButton('type', callback_data='46')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='47')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '42')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Reverse Giraffe')

@dp.callback_query_handler(lambda c: c.data == '43')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Dead')

@dp.callback_query_handler(lambda c: c.data == '44')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alien')

@dp.callback_query_handler(lambda c: c.data == '45')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Earth, Replacement Dimension')

@dp.callback_query_handler(lambda c: c.data == '46')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Parasite')

@dp.callback_query_handler(lambda c: c.data == '47')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

##################

@dp.message_handler(commands=['birdperson'])
async def birdperson_img(message: types.Message):
    btn = KeyboardButton('1')
    mk_bnt = ReplyKeyboardMarkup().add(btn)
    await bot.send_sticker(message.from_user.id, birdperson.read(),
                           reply_to_message_id=message.message_id,
                           reply_markup=mk_bnt)
    inl_btn0 = InlineKeyboardButton('name', callback_data='48')
    inl_btn = InlineKeyboardButton('status', callback_data='49')
    inl_btn1 = InlineKeyboardButton('species', callback_data='50')
    inl_btn2 = InlineKeyboardButton('location', callback_data='51')
    inl_btn3 = InlineKeyboardButton('type', callback_data='52')
    inl_btn4 = InlineKeyboardButton('gender', callback_data='53')
    inl_bnt_mk = InlineKeyboardMarkup().add(inl_btn0, inl_btn, inl_btn1, inl_btn2, inl_btn3, inl_btn4)
    await message.answer('otvet', reply_markup=inl_bnt_mk)

@dp.callback_query_handler(lambda c: c.data == '48')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Birdperson')

@dp.callback_query_handler(lambda c: c.data == '49')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alive')

@dp.callback_query_handler(lambda c: c.data == '50')
async def call_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Alien')

@dp.callback_query_handler(lambda c: c.data == '51')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Planet Squanch')

@dp.callback_query_handler(lambda c: c.data == '52')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Bird-Person')

@dp.callback_query_handler(lambda c: c.data == '53')
async def call_back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Male')

if __name__ == '__main__':
    executor.start_polling(dp)





