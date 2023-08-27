from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from . import config

# bot = Bot(token=config.BOT_TOKEN, proxy="http://proxy.server:3128")

storage = MemoryStorage()

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")
