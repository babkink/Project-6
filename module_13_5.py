
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_start = KeyboardButton(text='Calculate')
button_info = KeyboardButton(text='Info')
# kb.add(button_start)
# kb.add(button_info)
kb.row(button_start,button_info)

class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()

@dp.message_handler(text=['start'])
async def start(message):
    await message.answer('Hello, please select an action', reply_markup=kb)

    @dp.message_handler(text='Info')
    async def info(message):
        await message.answer('This bot calculates calories per day to keep your weight stable')

@dp.message_handler(text='Calculate')
async def set_age(message):
    await message.answer('Hello, please enter your age, full years')
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