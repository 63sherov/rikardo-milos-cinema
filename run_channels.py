import logging

from aiogram.types import Message

from func import save_channel, open_channel, open_admin
from loader import dp


@dp.message_handler(commands={'add_chan', 'rm_chan', 'all_chan'})
async def add_rm_all_command(message: Message):
    user_id = message.from_user.id
    command = message.get_command()

    channel_list = await open_channel()
    admin_list = await open_admin()

    if user_id not in admin_list:
        return True

    if command == '/all_chan':
        text = [f'<code>{i}</code>' for i in channel_list]
        text = '\n'.join(text)

        if not text:
            text = "Нет каналов!"

        await message.answer(text)
        return True

    try:
        channel = int(message.get_args())
    except ValueError:
        await message.answer(
            f"Вы ввели неверное значение!\nПример: {command} <code>-1001668139999</code>")
        return True

    if command == '/add_chan':
        if channel not in channel_list:
            channel_list.append(channel)
            await save_channel(channel_list)

            await message.answer(f'Канал <code>{channel}</code> добавлен')
            logging.info(f"ADMIN: user {user_id} add to admin {channel}")
        else:
            await message.answer(f'Канал {channel} уже был добавлен')

    elif command == '/rm_chan':
        if channel in channel_list:
            channel_list.remove(channel)
            await save_channel(channel_list)

            await message.answer(f'Канал <code>{channel}</code> удален')
            logging.info(f"ADMIN: user {user_id} rm from channel {channel}")
        else:
            await message.answer(f'Канал <code>{channel}</code> и так был удален')



