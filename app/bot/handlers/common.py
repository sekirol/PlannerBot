
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from ..state_machine import AppState

async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await state.set_state(AppState.initial)
    await message.answer("Приветствую!", reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_start, commands="cancel", state="*")
    dp.register_message_handler(cmd_start, Text(equals="отмена", ignore_case=True), state="*")