
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from ..state_machine import AppState

from . import messages

async def cmd_create(message: types.Message, state: FSMContext):
    await state.set_state(AppState.create)
    await message.answer(messages.create)

def register_handlers_create(dp: Dispatcher):
    dp.register_message_handler(cmd_create, commands="new", state=AppState.initial)