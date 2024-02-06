from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart, Command
from Utilities.db_controller import add_user, check_user_list

rt = Router()

@rt.message(CommandStart())
async def start_process(message: Message):
    add_user(message, is_admin = 1)
    await message.answer("Вы зарегистрировались")
    