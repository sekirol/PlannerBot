#!/usr/bin/env python3

import asyncio
import bot_tools

from aiogram import Bot, Dispatcher
from tools import get_access_data

async def main():
    bot = Bot(get_access_data("telegram"))
    dp = Dispatcher(bot)

    bot_tools.register_handlers(dp)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())