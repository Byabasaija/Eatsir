from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")
    await message.answer("Welcome to Eatsir 😄")
    await message.answer("You know what to do... Go ahead!")

    # Reply keyboard setup using ReplyKeyboardBuilder
    keyboard = ReplyKeyboardBuilder()
    keyboard.button("New here")
    keyboard.button("Login")
    keyboard.adjust(2)  # Adjust buttons into two columns

    # Send message with reply keyboard
    await message.answer("Choose an option:", reply_markup=keyboard.as_markup())

@dp.message(lambda message: message.text in ["New here", "Login"])
async def login_handler(message: types.Message):
    if message.text == "New here":
        # Handle new user scenario
        await message.answer("Welcome new user! Please register...")
        # Add your registration logic here
    elif message.text == "Login":
        # Handle login scenario
        await message.answer("Please enter your password:")
        # Add your login logic here

# Main function to start the bot
async def main() -> None:
    # Assign bot to the dispatcher
    dp.bot = bot
    await dp.start_polling()

# Entry point of the script
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
