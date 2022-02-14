import logging

from aiogram import types
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
import markups as nav
from func import check_member_channel, get_invite_link, open_admin, save_user_id
from loader import dp, bot
from run_channels import open_channel

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'], chat_type=types.ChatType.PRIVATE)
async def start(message: types.Message):

    await message.answer(
                           "🥤Все новинки фильмов 2022 доступны на нашем приватном канале.\n\n"
                           "📲Приятного просмотра 👇👇👇",
                           reply_markup=nav.startWatchMenu)
    await save_user_id(message.from_user.id)


@dp.callback_query_handler(text="start_watch", chat_type=types.ChatType.PRIVATE)
async def checksubquery(call: types.CallbackQuery):
    user_id = call.message.chat.id
    without_sub = ""
    step = 0
    channels = await open_channel()

    for channel_id in channels:
        member = await check_member_channel(channel_id, user_id)
        if not member:
            link = await get_invite_link(channel_id)
            if not link:
                continue
            step += 1

            without_sub += f"<b>Канал {step} -</b> {link}\n"

    if without_sub != "":
        with suppress(MessageNotModified):

            await call.message.edit_text(
                f"❌ ДОСТУП ЗАКРЫТ ❌\n\n👉Для доступа к приватному каналу нужно быть подписчиком <b>Кино-каналов.</b>\n\n"
                f"Подпишись на каналы ниже 👇 и нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n{without_sub}",
                reply_markup=nav.checkSubMenu, disable_web_page_preview=True)

    else:
        with suppress(MessageNotModified):

            await call.message.edit_text(
                "✅ ДОСТУП ОТКРЫТ\n\nВсе новинки 2022 сливаем на наш приватный канал. <b>Подпишись 👇</b>",
                reply_markup=nav.urlChannelMenu, disable_web_page_preview=True)


@dp.callback_query_handler(text="check_sub", chat_type=types.ChatType.PRIVATE)
async def checksubquery(call: types.CallbackQuery):
    # await bot.delete_message(message.from_user.id, message.message.message_id)

    user_id = call.message.chat.id
    without_sub = ""
    step = 0
    channels = await open_channel()

    for channel_id in channels:
        member = await check_member_channel(channel_id, user_id)
        if not member:
            link = await get_invite_link(channel_id)
            if not link:
                continue
            step += 1
            without_sub += f"<b>Канал {step} -</b> {link}\n"

    if without_sub != "":
        try:
            with suppress(MessageNotModified):

                await call.message.edit_text(
                    f"❌ ДОСТУП ЗАКРЫТ ❌\n\n👉Для доступа к приватному каналу нужно быть подписчиком <b>Кино-каналов.</b>"
                    f"\n\nПодпишись на каналы ниже 👇 и нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n{without_sub}",
                    reply_markup=nav.checkSubMenu, disable_web_page_preview=True)
                await call.answer("Вы подписались не на все каналы!")
        except:
            await call.answer("Вы не подписались ни на один из каналов!")
    else:
        with suppress(MessageNotModified):

            await call.message.edit_text(
                "✅ ДОСТУП ОТКРЫТ\n\nВсе новинки 2022 сливаем на наш приватный канал. <b>Подпишись 👇</b>",
                reply_markup=nav.urlChannelMenu, disable_web_page_preview=True)


@dp.message_handler(commands=['help'], chat_type=types.ChatType.PRIVATE)
async def help(message: types.Message):
    admins = await open_admin()

    if message.chat.id in admins:
        await message.answer("/all -> Показать id админов\n"
                             "/add <strong>user_id</strong> -> Добавить админа\n"
                             "/rm <strong>user_id</strong> -> Удалить админа\n\n"
                             "/all_chan -> Показать id каналов\n"
                             "/add_chan <strong>channel_id</strong> -> Добавить канал\n"
                             "/rm_chan <strong>channel_id</strong> -> Удалить канал\n")
