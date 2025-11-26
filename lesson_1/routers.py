from aiogram import Router, types        # Router — роутер сообщений, types — Telegram-объекты (Message, User и т.д.)
from aiogram.filters import CommandStart # фильтр, отлавливающий команду /start

user_router = Router()   # создаём отдельный роутер для пользовательских сообщений

# Обработчик команды /start
@user_router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    # message.from_user — объект пользователя, отправившего сообщение
    await message.answer(f'Привет {message.from_user.first_name}')  # отправляем приветствие

# Обработчик всех остальных сообщений
@user_router.message()
async def echo_message(message: types.Message) -> None:
    # простой echo-бот: отправляем назад то, что прислал пользователь
    await message.reply(message.text)
    # отдельное сообщение
    await message.answer(message.text)
