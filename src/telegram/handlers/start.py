from bot import dp
from aiogram import types

@dp.message_handler(commands=['start'])
async def info_message(message: types.Message):
    await message.reply('Hi!')
