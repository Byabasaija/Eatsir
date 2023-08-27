import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
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
        self.message_copy()


    def register_handlers(self):
        @self.dp.message_handler(CommandStart())
        async def command_start_handler(message: Message) -> None:
            info_user1 ='Seperate information about user one'
            info_user2 = 'Seperate information about user two'
        
            await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
            await message.answer(f"Please enter your password to access your daily plan")
   
        @self.dp.message_handler(content_types=types.ContentTypes.TEXT)
        async def get_password(message: types.Message):
            password = message.text
            print(password)
            await message.answer(f"{password} is your password")
    


    def message_copy(self):
        @self.dp.message_handler()
        async def echo_handler(self, message: types.Message) -> None:
        
            try:
        
                await message.send_copy(chat_id=message.chat.id)
            except TypeError:
                await message.answer("Nice try!")


    async def main(self) -> None:
        await self.dp.start_polling()



