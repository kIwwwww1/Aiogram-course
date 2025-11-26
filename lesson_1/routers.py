from aiogram import (Router,  
                     types) # types = типы Telegram-объектов (Message, Chat, User и др.)
from aiogram.filters import CommandStart # фильтр сообщений для команды /start

user_router = Router()

@user_router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(f'Привет {message.from_user.first_name}')

@user_router.message()
async def echo_message(message: types.Message) -> None:
    await message.reply(message.text)
