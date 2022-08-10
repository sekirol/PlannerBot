#!/usr/bin/env python3

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from tools import get_access_data

FSM_STORAGE_PATH = "app_state.json"

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

async def planning_handler(message: types.Message):
    await AppState.planning.set()
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Сейчас", callback_data="now"))

    await message.answer(f"*{message.text}*\n\n"
                          "Назначьте время старта:", reply_markup=keyboard, parse_mode="MarkdownV2")

async def planning_calback_handler(callback: types.CallbackQuery):
    await callback.answer("Test")

async def shutdown(dp: Dispatcher):
    await dp.storage.close()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, commands="start", state="*")
    dp.register_message_handler(cmd_new_handler, commands="new", state=AppState.initial)
    dp.register_message_handler(cmd_edit_handler, commands="edit", state=AppState.initial)

    dp.register_message_handler(planning_handler, state=AppState.create)
    dp.register_callback_query_handler(planning_calback_handler, state=AppState.planning)

class BotEngine:
    def __init__(self):
        pass

    def start(self):
        bot = Bot(get_access_data("telegram"))

        storage = JSONStorage(FSM_STORAGE_PATH)
        dp = Dispatcher(bot, storage=storage)

        register_handlers(dp)

        executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)