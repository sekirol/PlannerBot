
from aiogram.dispatcher.filters.state import State, StatesGroup

class AppState(StatesGroup):
    initial = State()
    create = State()
