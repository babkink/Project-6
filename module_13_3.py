
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Hello, I am bot to help you! ')

@dp.message_handler()
async def start(message):
    await message.answer('Please enter /start command to start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)