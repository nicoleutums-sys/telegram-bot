import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

API_TOKEN = os.getenv("8690071383:AAH6YZjkjBAR_CVNPk-2pTz8ttoDGf4Ocu88690071383:AAH6YZjkjBAR_CVNPk-2pTz8ttoDGf4Ocu8")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
