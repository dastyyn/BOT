from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

questionnaire_router = Router()


class Quest(StatesGroup):
    name = State()
    chosenAnime = State()
    favoritPerson = State()
    wathFrequency = State()


@questionnaire_router.message(Command("quest"))
async def start_quest(message: types.Message, state: FSMContext):
    await state.set_state(Quest.name)
    await message.answer('Введите ваше имя!!')


@questionnaire_router.message(Quest.name)
async def get_name(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer('Имя должно содержать не менее 3 букв')
        return
    await state.update_data(name=message.text)
    await state.set_state(Quest.chosenAnime)
    await message.answer('Ваше любимое аниме?')


@questionnaire_router.message(Quest.chosenAnime)
async def get_chosen_anime(message: types.Message, state: FSMContext):
    await state.set_state(Quest.favoritPerson)
    await message.answer('Ваш любимый персонаж?')


@questionnaire_router.message(Quest.favoritPerson)
async def get_favorit_anime(message: types.Message, state: FSMContext):
    await state.set_state(Quest.wathFrequency)
    kb = [
            [
                KeyboardButton(text="Часто"),
                KeyboardButton(text="Иногда")
            ],
            [
                KeyboardButton(text="Редко"),
                KeyboardButton(text="Не смотрю")
            ]
        ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Как часто вы смотрите аниме?', reply_markup=markup)


@questionnaire_router.message(Quest.wathFrequency)
async def get_wath_frequency(message: types.Message, state: FSMContext):
    frequency = message.text.lower()
    if frequency not in ["часто", "иногда", "редко", "не смотрю"]:
        await message.answer('Пожалуйста, выберите один из вариантов, используя кнопки на клавиатуре.')
        return
    await message.answer('Спасибо за ответы!')
    await state.clear()
