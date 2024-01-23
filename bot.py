from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
