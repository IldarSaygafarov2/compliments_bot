import random

from aiogram import types

from data.loader import bot, dp, scheduler
from data import config
from helpers.utils import read_json, read_file



@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    chat_id = message.chat.id

    await bot.send_message(
        chat_id,
        """
Привет, я не вижу тебя, я просто бот, но я уверен что смотря на тебя люди улыбаются твоей энерегетике.
Жмякни на команду /compliment
Надеюсь что смог поднять тебе настроение☻☻
""",
        parse_mode="HTML",
    )


@dp.message_handler(commands=["compliment"])
async def get_compliment(message: types.Message):
    chat_id = message.chat.id
    compliments = read_json("compliments.json")
    compliment = random.choice(compliments)[0].replace("\n ", "\n")
    await bot.send_message(chat_id, compliment)


@dp.message_handler()
async def send_compliment_by_me(message: types.Message):
    my_compliments = read_file("my_compliments.txt")
    compliment = random.choice(my_compliments).replace("\n ", "\n")
    await bot.send_message(config.MAIN_USER_ID, "А это для моей девочки♥")
    await bot.send_message(config.MAIN_USER_ID, compliment)


scheduler.add_job(send_compliment_by_me, "interval", seconds=21600, args=(types.Message,))


