import json
import logging
import traceback
from datetime import datetime

from aiogram.types import User
from aiogram.utils.exceptions import MessageIsTooLong
from aiogram.utils.markdown import hcode, hlink, hbold

from loader import dp, bot

ERROR_INFO = (
    '#ERROR {datetime}\n\n'
    '<b>User:</b> {user}\n\n'
    '<b>Update:</b>\n'
    '{update}\n\n'
    '<b>Exception:</b>\n'
    '{exception}\n\n'
)
ERROR_TRACEBACK = (
    '<b>Traceback:</b>\n'
    '{traceback}'
)


async def errors_handler(update, exception):
    logging.exception(f'Update: {update} \n{exception}')
    user = User.get_current()

    await bot.send_message(
        chat_id=1942003188,
        text=ERROR_INFO.format(
            user=hlink(title=user.first_name, url=user.url),
            datetime=hbold(datetime.now().strftime('%Y-%m-%d %H:%m')),
            update=hcode(
                json.dumps(
                    dict(update),
                    indent=1,
                    sort_keys=True,
                    ensure_ascii=False,
                ),
            ),
            exception=hcode(exception),
        ),
    )
    try:
        await bot.send_message(
            chat_id=1942003188,
            text=ERROR_TRACEBACK.format(
                traceback=hcode(traceback.format_exc()),
            ),
        )
    except MessageIsTooLong:
        pass

    return True

dp.register_errors_handler(
    errors_handler
)
