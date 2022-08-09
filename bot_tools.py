#!/usr/bin/env python3

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class AppState(StatesGroup):
    initial = State()
    planning = State()

async def cmd_start_handler(message: types.Message):
    await AppState.initial.set()

    initial_message = "Для начала работы выберите команду:\n" \
                      "*\/plan* \- перейти в режим планирования"

    await message.answer(initial_message, reply_markup=types.ReplyKeyboardRemove(), parse_mode="MarkdownV2")

async def cmd_plan_handler(message: types.Message):
    await AppState.planning.set()
    await message.answer("Опишите создаваемую задачу")

async def new_task_handler(message: types.Message):
    await message.answer(f"Создана задача:\n"
                         f"{message.text}\n"
                         f"Начало:\n"
                         f"Продолжительность:\n\n"
                         f"Вы можете создать ещё одну, или выйти,\n"
                         f"используя команду /start\n", parse_mode="MarkdownV2")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, commands="start", state="*")
    dp.register_message_handler(cmd_plan_handler, commands="plan", state=AppState.initial)
    dp.register_message_handler(new_task_handler, state=AppState.planning)