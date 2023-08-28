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

class BotHandler():
    def __init__(self):
        load_dotenv()
        self.TOKEN = getenv('TOKEN')
        self.bot = Bot(self.TOKEN, parse_mode=ParseMode.HTML)
        self.dp = Dispatcher(self.bot)

        # Register the handlers
        self.register_handlers()


    def register_handlers(self):
        @self.dp.message_handler(CommandStart())
        async def command_start_handler(message: Message) -> None:
            await message.answer(f"Hello, {hbold(message.from_user.first_name)}!")
            await message.answer(f"Welcome to Eatsir 😄", reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [types.KeyboardButton(text="Login")],
                    [types.KeyboardButton(text="Register")]
                ],
                resize_keyboard=True
            ))
        
        @self.dp.message_handler(content_types=types.ContentTypes.TEXT)
        async def login(message: types.Message):
            if message.text == "Login":
                # Perform login logic
                username = message.from_user.first_name
                await message.answer("Please enter your password:")
                password = message.text

                print(password)
                await message.answer("Hold on...")  # Show a message to indicate that the code is running
                user = Users.get_user(username, password)
                if user is not None:
                    # Display user info
                    await message.answer("Welcome back!")
                else:
                    # Ask if they want to get started
                    await message.answer("You are not yet in our system. Do you want to get started?")
            elif message.text == "Register":
                # Perform registration logic
                # Call the registration function here
                await self.register(message)


    async def main(self) -> None:
        await self.dp.start_polling()



