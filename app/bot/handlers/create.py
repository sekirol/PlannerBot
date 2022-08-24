
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

        context = {"task_info": task_info}
        await state.set_data(context)

        await message.answer(messages.create)

    async def new_task(self, message: types.Message, state: FSMContext) -> None:
        title = message.text.capitalize()
        groups = Planner.get_user_groups()

        keyboard = types.InlineKeyboardMarkup()
        for item in groups:
            keyboard.add(types.InlineKeyboardButton(item["name"], callback_data=item["id"]))

        answer_text = f"<b>{title}</b>\n\n" \
                      "Выберите категорию задачи:"

        await message.answer(answer_text, parse_mode="HTML", reply_markup=keyboard)

        context = await state.get_data()
        context["task_info"]["title"] = title
        context["groups"] = groups
        await state.update_data(context)
        
    async def task_edit_callback(self, query: types.CallbackQuery):
        await query.answer(query.data)
 
    def _register_handlers(self) -> None:
        self.dp.register_message_handler(self.cmd_create, commands="new", state=AppState.initial)
        self.dp.register_message_handler(self.new_task, state=AppState.create)
        self.dp.register_callback_query_handler(self.task_edit_callback, state=AppState.create)