from aiogram import Bot, Dispatcher

from . import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
