import asyncio
from aiogram.types import Message, Chat
from aiogram import Bot, Dispatcher
from Config.Config import load_config, Config
from handlers import user_handler, admin_handler, other_handler, chat_handler


async def main():
    config = load_config()
    bot  = Bot(token= config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_handler.rt)
    dp.include_router(admin_handler.rt)
    dp.include_router(chat_handler.rt)
    dp.include_router(other_handler.rt)
    
    await bot.delete_webhook()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
if __name__ == "__main__":
    asyncio.run(main())