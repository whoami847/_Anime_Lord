from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_callback_query(filters.regex("about"))
async def about_callback(client, callback_query):
    about_text = (
        "ᴀᴍᴀʀ ɴᴀᴍ: ᴀɴɪᴍᴇ ʟᴏʀᴅ\n"
        "ᴀᴅᴠᴀɴᴄᴇ ғɪᴄʜᴀʀ: (ʟɪɴᴋ)\n"
        "ᴍᴀʟɪᴋ: ᴋɪɴɢ\n"
        "ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3\n"
        "ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ V2\n"
        "ᴅᴀᴛᴀʙᴀsᴇ: ᴍᴏɴɢᴏ ᴅʙ\n"
        "ᴅᴇᴠᴇʟᴏᴘᴇʀ: @shidoteshika1"
    )
    buttons = [
        [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back_to_start")],
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]
    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/about.jpg"),
        caption=await to_smallcaps(about_text),
        reply_markup=InlineKeyboardMarkup(buttons)
  )
