from aiogram.types import Message
from aiogram import Router
from filter.filter import IsAdmin
from aiogram.filters import Command
from Utilities.db_controller import check_user_list

rt = Router()
rt.message.filter(IsAdmin())

@rt.message(Command("check"))
async def check_process(message : Message):
    await message.answer(check_user_list())

@rt.message(Command("setup"))
async def setup_process(message : Message):
    await message.answer("check")