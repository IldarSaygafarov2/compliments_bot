from aiogram import executor

import handlers
from data.loader import dp

if __name__ == "__main__":
    print("bot working")
    executor.start_polling(dp)
