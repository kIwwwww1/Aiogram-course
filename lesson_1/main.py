import asyncio # базовая библиотека Python для асинхронного исполнения
import logging # вывод служебных сообщений
from os import getenv
from dotenv import load_dotenv
from aiogram import (Bot, # объект для взаимодействия с Telegram API
                     Dispatcher) # маршрутизатор событий (апдейтов)

#  
from lesson_1.routers import user_router

load_dotenv()

USER_TOKEN = str(getenv('TOKEN'))

# Инициализация
bot = Bot(token=USER_TOKEN)
dp = Dispatcher()

async def main():
    print('Бот запущен')
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(user_router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())