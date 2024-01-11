import os
import random

from aiogram import Bot, Router, types
from aiogram.filters import Command

from bot import bot


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture(message: types.Message):
    file_list = os.listdir('images')
    random_file = random.choice(file_list)
    file_path = os.path.join('images', random_file)

    photo = types.FSInputFile(file_path)

    await bot.send_photo(chat_id=message.chat.id, photo=photo)

    
