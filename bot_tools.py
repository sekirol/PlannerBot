#!/usr/bin/env python3

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup

class AppState(StatesGroup):
    initial = State()
    create = State()
    edit = State()
    planning = State()

async def cmd_start_handler(message: types.Message):
    await AppState.initial.set()

    initial_message = "Для начала работы выберите команду:\n" \
                      "*\/new* \- создание задачи\n" \
                      "*\/edit* \- редактирование задач"

    await message.answer(initial_message, reply_markup=types.ReplyKeyboardRemove(), parse_mode="MarkdownV2")

async def cmd_new_handler(message: types.Message):
    await AppState.create.set()
    await message.answer("Назовите задачу")

async def cmd_edit_handler(message: types.Message):
    await AppState.edit.set()
    await message.answer("Выберите задачу для редактирования")

async def new_task_handler(message: types.Message):
    await message.answer("Создана задача:\n"
                        f"{message.text}")

async def shutdown(dp: Dispatcher):
    await dp.storage.close()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, commands="start", state="*")
    dp.register_message_handler(cmd_new_handler, commands="new", state=AppState.initial)
    dp.register_message_handler(cmd_edit_handler, commands="edit", state=AppState.initial)

    dp.register_message_handler(new_task_handler, state=AppState.create)