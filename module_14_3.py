
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import *
from keyboards import *
import text
from text import products

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

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
    for product in products.items():
        with open(product[1][1], 'rb') as img:
            await message.answer_photo(img, product[1][0])
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)