import json

from loader import bot


async def save_user_id(user_id: int):
    with open("user_id.json", "r") as file:
        user_list = json.load(file)

    if user_id not in user_list:
        user_list.append(user_id)
        with open("user_id.json", "w") as file:
            json.dump(user_list, file)


async def check_member_channel(channel_id, user_id):
    try:
        chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    except:
        return True

    if chat_member['status'] != 'left':
        return True
    else:
        return False


async def get_invite_link(channel_id):
    try:
        chat = await bot.get_chat(channel_id)
    except:
        return False
    if chat.username is None:
        link = chat.invite_link
    else:
        link = f'@{chat.username}'

    return link


async def save_admin(channel):
    with open("admin.json", "w") as file:
        json.dump(channel, file)


async def open_admin():
    with open("admin.json", "r") as file:
        admin_list = json.load(file)
    return admin_list


async def save_channel(channel):
    with open("channel.json", "w") as file:
        json.dump(channel, file)


async def open_channel():
    with open("channel.json", "r") as file:
        admin_list = json.load(file)
    return admin_list
