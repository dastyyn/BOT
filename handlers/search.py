from aiogram import Router, types, F
from aiogram.filters import Command
from db.queries import get_anime_by_genre

search_router = Router()


@search_router.message(Command("search"))
async def search(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Detective"),
            types.KeyboardButton(text="Senen"),
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


@search_router.message(F.text == "Detective")
async def detective(message: types.Message):
    genre = "Detective"
    anime_list = get_anime_by_genre(genre)
    kb = types.ReplyKeyboardRemove()
    for anime in anime_list:
        await message.answer(anime[0], reply_markup=kb)


@search_router.message(F.text == "Senen")
async def senen(message: types.Message):
    genre = "Senen"
    anime_list = get_anime_by_genre(genre)
    kb = types.ReplyKeyboardRemove()
    for anime in anime_list:
        await message.answer(anime[0], reply_markup=kb)


@search_router.message(F.text == "Romance")
async def romance(message: types.Message):
    genre = "Romance"
    anime_list = get_anime_by_genre(genre)
    kb = types.ReplyKeyboardRemove()
    for anime in anime_list:
        await message.answer(anime[0], reply_markup=kb)


@search_router.message(F.text == "Isekai")
async def isekai(message: types.Message):
    genre = "Isekai"
    anime_list = get_anime_by_genre(genre)
    kb = types.ReplyKeyboardRemove()
    for anime in anime_list:
        await message.answer(anime[0], reply_markup=kb)
