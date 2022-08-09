#!/usr/bin/env python3

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
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

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add("Список актуальных задач")

    await message.answer("Опишите создаваемую задачу", reply_markup=keyboard)

async def new_task_handler(message: types.Message):
    await message.answer(f"Создана задача:\n"
                         f"{message.text}\n"
                         f"Начало:\n"
                         f"Продолжительность:\n\n"
                         f"Вы можете создать ещё одну, или выйти,\n"
                         f"используя команду /start\n", parse_mode="MarkdownV2")

async def actual_list_handler(message: types.Message):
    await message.answer("Актуальные задачи:")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, commands="start", state="*")
    dp.register_message_handler(cmd_plan_handler, commands="plan", state=AppState.initial)
    dp.register_message_handler(actual_list_handler, Text(equals="Список актуальных задач", ignore_case=True), state=AppState.planning),
    dp.register_message_handler(new_task_handler, state=AppState.planning)