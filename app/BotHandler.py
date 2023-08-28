import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from app.Users import Users
from dotenv import load_dotenv
from aiogram import types

load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def start_handler(message: types.Message):
    if message.text.lower() == "start":
        await message.answer(f"Hello, {hbold(message.from_user.first_name)}!")
        await message.answer(f"Welcome to Eatsir 😄")    
        await message.answer(f"You know what to do... Go ahead!")  

     
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def login_handler(message: types.Message):
        print('hello')
        password =  message.text
        username = message.from_user.first_name
    
        await message.answer(f"Hold on...")
        user = Users.get_user(username, password)
        if user is not None:
            # Display user info
            await message.answer("Welcome back!")
        else:
            # Ask if they want to get started
            await message.answer("Looks like you don't know what to do!")
            await message.answer("Input your passocode or create one 👇", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Create"))

async def main() -> None:
    await dp.start_polling()
