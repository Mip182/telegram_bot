from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi!\nWrite me smthing!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write me smthing and I will send you this text!")

@dp.message_handler(commands=['voice'])
async def process_help_command(message: types.Message):
    await message.reply("Voice!!")

@dp.message_handler(commands=['group'])
async def process_help_command(message: types.Message):
    await message.reply("Group!!")

@dp.message_handler(commands=['note'])
async def process_help_command(message: types.Message):
    await message.reply("Note!!")

@dp.message_handler(commands=['file'])
async def process_help_command(message: types.Message):
    await message.reply("File!!")    

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
