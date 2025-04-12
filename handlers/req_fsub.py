from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("req_fsub") & filters.user(ADMIN_IDS))
async def req_fsub_command(client, message):
    settings = get_settings()
    req_fsub_text = f"ʀᴇQᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ: {'ᴄʜᴀʟᴜ' if settings['request_fsub'] else 'ʙᴏɴᴅʜ'}, ɴɪᴄʜᴇʀ ʙᴀᴛᴏɴᴇ ᴋʟɪᴄᴋ ᴋᴏʀᴇ sᴇᴛɪɴɢs ᴘᴏʀɪʙᴏʀᴛᴏɴ ᴋᴏʀᴏ।"
    buttons = [
        [InlineKeyboardButton("ᴏɴ", callback_data="req_fsub_on")],
        [InlineKeyboardButton("ᴏғғ", callback_data="req_fsub_off")],
        [InlineKeyboardButton("ᴍᴏʀᴇ sᴇᴛᴛɪɴɢs", callback_data="more_settings")]
    ]
    await message.reply(await to_smallcaps(req_fsub_text), reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("req_fsub_on"))
async def req_fsub_on(client, callback_query):
    update_settings({"request_fsub": True})
    await callback_query.message.edit(await to_smallcaps("ʀᴇQᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ ᴄʜᴀʟᴜ ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))

@Client.on_callback_query(filters.regex("req_fsub_off"))
async def req_fsub_off(client, callback_query):
    update_settings({"request_fsub": False})
    await callback_query.message.edit(await to_smallcaps("ʀᴇQᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ ʙᴏɴᴅʜ ᴋᴏʀᴀ ʜᴏʏᴇᴄʜᴇ!"))
