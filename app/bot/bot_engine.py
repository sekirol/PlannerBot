#!/usr/bin/env python3

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import PickleStorage

from .handlers.basic import BasicHandlers
from .handlers.create import CreateMenuHandlers

from ..tools import get_access_data
from ..planner import Planner

FSM_STORAGE_PATH = "../data/app_state.bin"

async def shutdown(dp: Dispatcher):
    await dp.storage.close()

class BotEngine:
    def __init__(self):
        bot = Bot(get_access_data("telegram"))
        storage = PickleStorage(FSM_STORAGE_PATH)
        
        self.dp = Dispatcher(bot, storage=storage)

        self.planner = Planner()

        self._init_handlers()

    def _init_handlers(self):
        handlers = [
            BasicHandlers(self.dp),
            CreateMenuHandlers(self.dp, self.planner)
        ]

    def start(self):
        executor.start_polling(self.dp, skip_updates=True, on_shutdown=shutdown)
