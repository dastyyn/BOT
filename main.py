import asyncio
import logging

from aiogram.types import BotCommand
from bot import bot, dp, Admin, scheduler
from handlers import (my_info_router, picture_router, start_router,
                    search_router, questionnaire_router)
from db.queries import init_db, create_tables, populate_db
from parserr import parser_router


logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    try:
        for i in Admin:
            await bot.send_message(chat_id=i, text="Бот запущен")

        print("Bot is launched.")

        await bot.set_my_commands(
            [
                BotCommand(command="start", description="Начать"),
                BotCommand(command="my_info", description="Информация о пользователе"),
                BotCommand(command="picture", description="Случайная картинка"),
                BotCommand(command="search", description="Поиск аниме по жанру"),
                BotCommand(command="quest", description="Опрос")
            ]
        )


        init_db()
        create_tables()
        # populate_db()



        dp.include_router(start_router)
        dp.include_router(questionnaire_router)
        dp.include_router(my_info_router)
        dp.include_router(picture_router)
        dp.include_router(parser_router)
        
        # dp.include_router(search_router)


        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error on startup: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_startup(dp))
