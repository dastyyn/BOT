from aiogram import Router, types, F
from aiogram.filters import Command
from db.queries import get_anime_by_genre_name


search_router = Router()


@search_router.message(Command("search"))
async def search(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Detective"),
            types.KeyboardButton(text="Shonen"),
        ],
        [
            types.KeyboardButton(text="Romance"),
            types.KeyboardButton(text="Isekai")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Choose anime genre:", reply_markup=keyboard)



@search_router.message(F.text)
async def handle_genre(message: types.Message):
    valid_genres = ["Detective", "Shonen", "Romance", "Isekai"]
    
    if message.text in valid_genres:
        genre = message.text
        anime_list = get_anime_by_genre_name(genre)
        kb = types.ReplyKeyboardRemove()
        for anime in anime_list:
            await message.answer(anime[0], reply_markup=kb)
    else:
        await message.answer("Invalid genre. Please choose a valid genre from the provided options.")
