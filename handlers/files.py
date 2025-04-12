from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("files") & filters.user(ADMIN_IDS))
async def files_command(client, message):
    settings = get_settings()
    files_text = (
        f"ᴋᴏɴᴛᴇɴᴛ ᴘʀᴏᴛᴇᴋᴛ: {'ᴄʜᴀʟᴜ' if settings['protect_content'] else 'ʙᴏɴᴅʜ'}\n"
        f"ʜᴀɪᴅ ᴋᴀᴘsʜᴀɴ: {'ᴄʜᴀʟᴜ' if settings['hide_caption'] else 'ʙᴏɴᴅʜ'}\n"
        f"ᴄʜᴀɴᴇʟ ʙᴀᴛᴏɴ: {'ᴄʜᴀʟᴜ' if settings['channel_button'] else 'ʙᴏɴᴅʜ'}\n"
        "ɴɪᴄʜᴇʀ ʙᴀᴛᴏɴᴇ ᴋʟɪᴄᴋ ᴋᴏʀᴇ sᴇᴛɪɴɢs ᴘᴏʀɪʙᴏʀᴛᴏɴ ᴋᴏʀᴏ।"
    )
    buttons = [
        [InlineKeyboardButton("ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("sᴇᴛ ʙᴜᴛᴛᴏɴ", callback_data="set_button")],
        [InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="refresh_files")],
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]
    await message.reply_photo(
        photo="images/files.jpg",
        caption=await to_smallcaps(files_text),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("toggle_protect_content"))
async def toggle_protect_content(client, callback_query):
    settings = get_settings()
    new_value = not settings["protect_content"]
    update_settings({"protect_content": new_value})
    await callback_query.message.edit(await to_smallcaps(f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ {'ᴄʜᴀʟᴜ' if new_value else 'ʙᴏɴᴅʜ'} ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))

@Client.on_callback_query(filters.regex("toggle_hide_caption"))
async def toggle_hide_caption(client, callback_query):
    settings = get_settings()
    new_value = not settings["hide_caption"]
    update_settings({"hide_caption": new_value})
    await callback_query.message.edit(await to_smallcaps(f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ {'ᴄʜᴀʟᴜ' if new_value else 'ʙᴏɴᴅʜ'} ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))

@Client.on_callback_query(filters.regex("toggle_channel_button"))
async def toggle_channel_button(client, callback_query):
    settings = get_settings()
    new_value = not settings["channel_button"]
    update_settings({"channel_button": new_value})
    await callback_query.message.edit(await to_smallcaps(f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ {'ᴄʜᴀʟᴜ' if new_value else 'ʙᴏɴᴅʜ'} ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))
