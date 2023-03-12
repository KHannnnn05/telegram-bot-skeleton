from bot import dp
from aiogram import types

@dp.message_handler(commands=['info'])
async def info_message(message: types.Message):
    await message.reply('I was developed at ashm.tech')
