from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL

btnStartWatch = InlineKeyboardButton(text="🥤 НАЧАТЬ СМОТРЕТЬ 🥤", callback_data="start_watch")
startWatchMenu = InlineKeyboardMarkup(row_width=1)
startWatchMenu.insert(btnStartWatch)

btnCheckSub = InlineKeyboardButton(text="🥤 Я ПОДПИСАЛСЯ 🥤", callback_data="check_sub")
checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnCheckSub)

btnUrl = InlineKeyboardButton(text="🥤 ПОДПИСАТЬСЯ 🥤", url=CHANNEL)
urlChannelMenu = InlineKeyboardMarkup(row_width=1)
urlChannelMenu.insert(btnUrl)
