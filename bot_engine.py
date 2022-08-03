#!/usr/bin/env python3

from aiogram import Bot, Dispatcher, executor, types
from tools import get_access_data

bot = Bot(get_access_data("telegram"))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

def start():
    executor.start_polling(dp, skip_updates=True)