from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("auto_del") & filters.user(ADMIN_IDS))
async def auto_del_command(client, message):
    settings = get_settings()
    auto_del_text = (
        f"ᴀᴜᴛᴏ-ᴅɪʟɪᴛ ᴍᴏᴅᴇ: {'ᴄʜᴀʟᴜ' if settings['auto_delete'] else 'ʙᴏɴᴅʜ'}\n"
        f"ᴅɪʟɪᴛ ᴛᴀɪᴍᴀʀ: {settings['delete_timer'] // 3600} ɢʜᴏɴᴛᴀ\n"
        "ɴɪᴄʜᴇʀ ʙᴀᴛᴏɴᴇ ᴋʟɪᴄᴋ ᴋᴏʀᴇ sᴇᴛɪɴɢs ᴘᴏʀɪʙᴏʀᴛᴏɴ ᴋᴏʀᴏ।"
    )
    buttons = [
        [InlineKeyboardButton("ᴅɪsᴀʙʟᴇ ᴍᴏᴅᴇ", callback_data="disable_auto_delete")],
        [InlineKeyboardButton("sᴇᴛ ᴛɪᴍᴇʀ", callback_data="set_timer")],
        [InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="refresh_auto_del")],
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]
    await message.reply_photo(
        photo="images/auto_del.jpg",
        caption=await to_smallcaps(auto_del_text),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("disable_auto_delete"))
async def disable_auto_delete(client, callback_query):
    update_settings({"auto_delete": False})
    await callback_query.message.edit(await to_smallcaps("ᴀᴜᴛᴏ-ᴅɪʟɪᴛ ᴍᴏᴅᴇ ʙᴏɴᴅʜ ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))

@Client.on_callback_query(filters.regex("set_timer"))
async def set_timer(client, callback_query):
    update_settings({"delete_timer": 7200})  # Example: 2 hours
    await callback_query.message.edit(await to_smallcaps("ᴅɪʟɪᴛ ᴛᴀɪᴍᴀʀ 2 ɢʜᴏɴᴛᴀ ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))
