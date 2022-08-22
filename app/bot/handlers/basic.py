
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from ..state_machine import AppState

from . import messages

class BasicHandlers:
    """
    Basic command handlers
    """

    def __init__(self, dp) -> None:
        self.dp = dp

        self._register_handlers()

    async def cmd_start(self, message: types.Message, state: FSMContext) -> None:
        await state.finish()
        await state.set_state(AppState.initial)
        await message.answer(messages.initial, reply_markup=types.ReplyKeyboardRemove())

    def _register_handlers(self) -> None:
        self.dp.register_message_handler(self.cmd_start, commands="start", state="*")
        self.dp.register_message_handler(self.cmd_start, commands="cancel", state="*")
        self.dp.register_message_handler(self.cmd_start, Text(equals="отмена", ignore_case=True), state="*")