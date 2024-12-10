from pyrogram import filters
from pyrogram.types import Message

from TS import app
from TS.core.call import Anony
from TS.utils.database import set_loop
from TS.utils.decorators import AdminRightsCheck
from TS.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "bitir", "cend", "kapat"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Anony.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
