from aiogram import Bot, Dispatcher

from . import config


bot = Bot(token=config.BOT_TOKEN, proxy="http://proxy.server:3128")
dp = Dispatcher(bot)
