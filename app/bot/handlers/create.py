
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from ..state_machine import AppState

from . import messages

class CreateMenuHandlers:
    """
    Command handlers of create menu item 
    """

    def __init__(self, dp) -> None:
        self.dp = dp

        self._register_handlers()
        
    async def cmd_create(self, message: types.Message, state: FSMContext) -> None:
        await state.set_state(AppState.create)
        await message.answer(messages.create)

    def _register_handlers(self) -> None:
        self.dp.register_message_handler(self.cmd_create, commands="new", state=AppState.initial)