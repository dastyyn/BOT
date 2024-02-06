from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
Admin = [974896300, ]
scheduler = AsyncIOScheduler()
