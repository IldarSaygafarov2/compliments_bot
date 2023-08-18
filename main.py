from aiogram import executor

from data.loader import dp, scheduler
import handlers

if __name__ == "__main__":
    print("bot working")
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
