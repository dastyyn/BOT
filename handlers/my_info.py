from aiogram import Router, types
from aiogram.filters import Command


my_info_router = Router()


@my_info_router.message(Command("my_info"))
async def my_info(message: types.Message):
    await message.answer(f"Your id: {message.from_user.id}\n"
                        f"your first name is {message.from_user.first_name}\n"
                        f"your username is {message.from_user.username}\n")
