from bot import dp
from aiogram import types

@dp.message_handler(commands=['help'])
async def info_message(message: types.Message):
    await message.reply('How I can help you?!')
