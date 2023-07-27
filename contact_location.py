import logging
from aiogram import Dispatcher, Bot, executor, types

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6008616711:AAETe8g9GM3M9fgPrdpAh6T6vGWpWJJhrSw"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
menu.add(
    types.KeyboardButton("Telefon raqam", request_contact=True),
    types.KeyboardButton("Manzil", request_location=True),
)

@dp.message_handler(content_types=['contact'])
async def get_contact(message: types.Message):
    phone_number = message.contact.phone_number
    await message.answer(f"<b><u>{phone_number}</u></b>")

async def location_inline_btn(url):
    location_btn = types.InlineKeyboardMarkup()
    location_btn.add(
        types.InlineKeyboardButton("Xavola", url=url)
    )
    return location_btn

@dp.message_handler(content_types=['location'])
async def get_loaction(message: types.Message):
    loc = message.location
    map_url = f"https://www.google.com/maps/@{loc.latitude},{loc.longitude}"
    btn = await location_inline_btn(map_url)
    await message.answer("Sizning xavolangiz:", reply_markup=btn)

@dp.message_handler(commands=['contact'])
async def send_contact_handler(message: types.Message):
    await message.answer_contact(phone_number="+998913451175", first_name="Winchestor")


@dp.message_handler(commands=['location'])
async def send_location_handler(message: types.Message):
    await message.answer_location(latitude=75.254236, longitude=18.25325@dp.message_handler(commands=['contact'])
async def send_contact_handler(message: types.Message):
    await message.answer_contact(phone_number="+998913451175", first_name="Winchestor")


@dp.message_handler(commands=['location'])
async def send_location_handler(message: types.Message):
    await message.answer_location(latitude=75.254236, longitude=18.25325


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Salom", reply_markup=menu)



if __name__ == '__main__':
    executor.start_polling(dp)