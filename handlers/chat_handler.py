from email import message
from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated
from Utilities.chat_settings import reg_chat, select_chat

rt = Router()

@rt.my_chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def join_chat_process(chat_mem : ChatMemberUpdated):
    reg_chat(message = chat_mem)
    await chat_mem.answer("Вы добавили на сервер бота")
    #await chat_mem.answer(select_chat())
    
@rt.my_chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER << IS_MEMBER))
async def left_chat_process():
    print("Бот удален")