from email.policy import default

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    print('I am bot to help you!')

@dp.message_handler()
async def start(message):
    print('Please enter /start command to start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)