from aiogram import Bot, Dispatcher
import config as cfg


bot = Bot(token=cfg.TOKEN, parse_mode="html")
dp = Dispatcher(bot)
