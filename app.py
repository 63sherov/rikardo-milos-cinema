from aiogram.utils import executor

from loader import dp
from func import open_admin

import main
import run_channels
import run_admin
import errors


async def on_startup(dp):
    admins = await open_admin()

    for admin in admins:
        try:
            await dp.bot.send_message(admin, 'Бот запущен ❗️')
        except:
            pass


async def on_shutdown(dp):
    admins = await open_admin()

    for admin in admins:
        try:
            await dp.bot.send_message(admin, 'Бот остановлен ❗️')
        except:
            pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
