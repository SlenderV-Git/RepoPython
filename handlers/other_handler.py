from aiogram.types import Message
from aiogram import Router
from Lexicon.lexicon import MESSAGE_LIST

rt = Router()

@rt.message()
async def unknow_user(message : Message):
    await message.answer(MESSAGE_LIST["unknow_user"])

