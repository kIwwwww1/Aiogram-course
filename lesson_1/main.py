import asyncio              # базовая библиотека Python для асинхронного исполнения
import logging              # вывод служебных сообщений
from os import getenv       # функция для получения переменных окружения
from dotenv import load_dotenv  # загрузка переменных из .env файла
from aiogram import Bot, Dispatcher  # Bot — взаимодействие с Telegram API, Dispatcher — маршрутизатор событий

# Импорт внешних обработчиков (роутера)
from lesson_1.routers import user_router

load_dotenv()  # загружаем значения из .env при старте приложения

USER_TOKEN = str(getenv('TOKEN'))  # достаём токен бота из переменной окружения

# Инициализация бота и диспетчера
bot = Bot(token=USER_TOKEN)        # создаём объект бота
dp = Dispatcher()                  # создаём диспетчер — он распределяет апдейты по обработчикам

async def main():
    print('Бот запущен')  # простое уведомление в консоли

    # Удаляем старый вебхук (если он был) и очищаем очередь обновлений
    await bot.delete_webhook(drop_pending_updates=True)

    # Подключаем роутеры (внешние обработчики сообщений)
    dp.include_router(user_router)

    # Настраиваем логирование (для отладки и контроля работы бота)
    logging.basicConfig(level=logging.INFO)

    # Запускаем постоянный опрос Telegram-серверов
    await dp.start_polling(bot)

# Точка входа в приложение
if __name__ == '__main__':
    asyncio.run(main())  # запускаем асинхронную функцию main()
