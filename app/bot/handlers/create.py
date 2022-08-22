
import pprint

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from ...planner import Planner
from ..state_machine import AppState
from . import messages

class CreateMenuHandlers:
    """
    Command handlers of create menu item 
    """

    def __init__(self, dp: Dispatcher, planner: Planner) -> None:
        self.dp = dp
        self.planner = planner

        self._register_handlers()
        
    async def cmd_create(self, message: types.Message, state: FSMContext) -> None:
        await state.set_state(AppState.create)

        task_info = {
            "title": None,
            "group": None,
            "duration": None,
            "start": None
        }
        await state.set_data(task_info)

        await message.answer(messages.create)

    async def new_task(self, message: types.Message, state: FSMContext) -> None:
        task_info = await state.get_data()

        task_info["title"] = message.text

        await message.answer(pprint.pformat(task_info, width=1, sort_dicts=False))
        await state.update_data(task_info)
        
    def _register_handlers(self) -> None:
        self.dp.register_message_handler(self.cmd_create, commands="new", state=AppState.initial)
        self.dp.register_message_handler(self.new_task, state=AppState.create)