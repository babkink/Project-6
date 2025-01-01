
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import *
from keyboards import *
import text
from functions import get_all_products, add_user, is_user_exist

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(text='start')
async def main_menu(message):
    await message.answer(text.start_message, reply_markup=start_kb)

@dp.message_handler(text=['about'])
async def start(message):
    await message.answer(text.about_message, reply_markup=start_kb)

@dp.message_handler(text=['price'])
async def start(message):
    await message.answer('What would you like?', reply_markup=catalog_kb)

@dp.message_handler(text='BUY')
async def get_buying_list(message):
    for product in get_all_products():
        with open(product[4], 'rb') as img:
            await message.answer_photo(img, f'{product[1]} | {product[2]} | Price: {product[3]}')
    await message.answer('Please make a choice!', reply_markup=buy_2_kb)

@dp.callback_query_handler(text='beginners')
async def buy_b(call):
    await call.message.answer(text.message_10, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='normal')
async def buy_n(call):
    await call.message.answer(text.message_20, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='advanced')
async def buy_a(call):
    await call.message.answer(text.message_30, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='super')
async def buy_s(call):
    await call.message.answer(text.message_40, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_(call):
    await call.message.answer(text.message_other, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('You successfully bought the product!')
    await call.answer()

@dp.message_handler(text='Sign Up')
async def sign_up(message):
    await RegistrationState.username.set()
    await message.answer('Please enter user name (latin letters ONLY)')

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if not is_user_exist(message.text):
        RegistrationState.username = message.text
        await RegistrationState.email.set()
        await message.answer('Please enter your email in format "name@provider.com')
    else:
        await message.answer(f'User with username "{message.text}" already exists, please choose another username)')
        await RegistrationState.username.set()
        await message.answer('Please enter user name (latin letters ONLY)')

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    RegistrationState.email = message.text
    await RegistrationState.age.set()
    await message.answer('Please enter your age')

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    RegistrationState.age = message.text
    await state.finish()
    add_user(RegistrationState.username, RegistrationState.email, RegistrationState.age)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)