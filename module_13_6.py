
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_start = KeyboardButton(text='Calculate')
button_info = KeyboardButton(text='Info')
kb.row(button_start,button_info)

inl_kb = InlineKeyboardMarkup()
button_calc = InlineKeyboardButton(text='Calculate calories', callback_data='calories')
button_formula = InlineKeyboardButton(text='Show formula', callback_data='formulas')
inl_kb.row(button_calc, button_formula)

class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()

@dp.message_handler(text='Calculate')
async def main_menu(message):
    await message.answer('select option', reply_markup=inl_kb)

@dp.message_handler(text=['start'])
async def start(message):
    await message.answer('Hello, please select an action', reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('amount calories a day = 5 * age, full years + 6.25 * height in cm + 10 * weight in kg + 5')


@dp.message_handler(text='Info')
async def info(message):
    await message.answer('This bot calculates calories per day to keep your weight stable')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Hello, please enter your age, full years')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=message.text)
    await message.answer('Please enter your height in cm')
    await UserState.height.set()

@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Please enter your weight in kg')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def calculate_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 5 * int(data["age"]) + 6.25 * int(data["height"]) + 10 * int(data["weight"]) + 5
    await message.answer(f'Daily calories consumption to keep weight is {calories}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)