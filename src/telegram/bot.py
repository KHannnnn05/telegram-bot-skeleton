import logging
from aiogram import Bot, Dispatcher
from config import token

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
