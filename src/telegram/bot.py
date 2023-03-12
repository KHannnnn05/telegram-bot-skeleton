import logging
from aiogram import Bot, Dispatcher
from config import test_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

memory_storage = MemoryStorage()
bot = Bot(test_token)
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)
