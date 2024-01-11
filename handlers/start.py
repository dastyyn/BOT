from aiogram import Router, types, F
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="О боте", callback_data="about"
                ),
                types.InlineKeyboardButton(
                    text="Контакты", callback_data="contact"
                )
            ], [
                types.InlineKeyboardButton(
                    text="Пасхалка", url="https://goo.su/oKxfb"     # ссылка безопасна

                )
            ]
        ]
    )
    await message.answer(
        f"Hello, {message.from_user.first_name}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def abot_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("О боте:\n"
                                "Бот создан для поиска аниме")


@start_router.callback_query(F.data == "contact")
async def us_contacts(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Контакты:\n"
                                "mail: dastyyyyyn@icloud.com\n"
                                "phone number: +996700263233")
