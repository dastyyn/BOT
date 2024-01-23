import asyncio

from aiogram.types import BotCommand
from dotenv import load_dotenv

from bot import bot, dp
from handlers import (my_info_router, picture_router, start_router,
                    search_router, questionnaire_router)


async def main():
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Начало"),
            BotCommand(command="my_info", description="Информация обо мне"),
            BotCommand(command="picture", description="Случайная картинка"),
            BotCommand(command="search", description="Каталог"),
            BotCommand(command="quest", description="Опрос")
        ]
    )

    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(picture_router)
    dp.include_router(search_router)
    dp.include_router(questionnaire_router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
