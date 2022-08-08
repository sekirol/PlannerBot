#!/usr/bin/env python3


from aiogram import Dispatcher, types

async def cmd_start_handler(message: types.Message):
    await message.answer("Для начала работы выберите одну из команд.")

async def cmd_planning_handler(message: types.Message):
    await message.answer("Режим планирования")
    
async def cmd_schedule_handler(message: types.Message):
    await message.answer("Режим просмотра графика")

async def cmd_statistic_handler(message: types.Message):
    await message.answer("Режим просмотра статистики")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, commands="start")
    dp.register_message_handler(cmd_planning_handler, commands="plan")
    dp.register_message_handler(cmd_schedule_handler, commands="shed")
    dp.register_message_handler(cmd_statistic_handler, commands="stat")
