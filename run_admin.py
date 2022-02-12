import logging

from aiogram.types import Message

from func import save_admin, open_admin
from loader import dp


@dp.message_handler(commands={'add', 'rm', 'all'})
async def add_rm_all_command(message: Message):
    user_id = message.from_user.id
    command = message.get_command()
    admin_list = await open_admin()

    if user_id not in admin_list:
        return True

    if command == '/all':
        text = [f'<code>{i}</code>' for i in admin_list]
        text = '\n'.join(text)

        if not text:
            text = "Нет админов!"  # лол, а как посмотреть тогда? Ладно :D

        await message.answer(text)
        return True

    try:
        admin = int(message.get_args())
    except ValueError:
        await message.answer(
            f"Вы ввели неверное значение!\nПример: {command} <code>1810326448</code>")
        return True

    if command == '/add':
        if admin not in admin_list:
            admin_list.append(admin)
            await save_admin(admin_list)

            await message.answer(f'Администратор <code>{admin}</code> добавлен')
            logging.info(f"ADMIN: user {user_id} add to admin {admin}")
        else:
            await message.answer(f'Администратор <code>{admin}</code> уже был добавлен')

    elif command == '/rm':
        if admin in admin_list:
            admin_list.remove(admin)
            await save_admin(admin_list)

            await message.answer(f'Администратор <code>{admin}</code> удален')
            logging.info(f"ADMIN: user {user_id} rm from channel {admin}")
        else:
            await message.answer(f'Администратор <code>{admin}</code> и так был удален')
