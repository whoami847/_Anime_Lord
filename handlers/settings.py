from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from database import get_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_callback_query(filters.regex("settings"))
async def settings_callback(client, callback_query):
    settings = get_settings()
    settings_text = (
        f"ᴍᴏᴛ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴᴇʟ: {len(settings['force_sub_channels'])}\n"
        "ᴍᴏᴛ ᴀᴅᴍɪɴ: 1\n"
        f"ᴍᴏᴛ ʙʏᴀɴᴅ ᴜsᴇʀ: {len(settings['banned_users'])}\n"
        f"ᴀᴜᴛᴏ-ᴅɪʟɪᴛ ᴍᴏᴅᴇ: {'ᴄʜᴀʟᴜ' if settings['auto_delete'] else 'ʙᴏɴᴅʜ'}\n"
        f"ᴋᴏɴᴛᴇɴᴛ ᴘʀᴏᴛᴇᴋᴛ: {'ᴄʜᴀʟᴜ' if settings['protect_content'] else 'ʙᴏɴᴅʜ'}\n"
        f"ʜᴀɪᴅ ᴋᴀᴘsʜᴀɴ: {'ᴄʜᴀʟᴜ' if settings['hide_caption'] else 'ʙᴏɴᴅʜ'}\n"
        f"ᴄʜᴀɴᴇʟ ʙᴀᴛᴏɴ: {'ᴄʜᴀʟᴜ' if settings['channel_button'] else 'ʙᴏɴᴅʜ'}\n"
        f"ʀᴇQᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ: {'ᴄʜᴀʟᴜ' if settings['request_fsub'] else 'ʙᴏɴᴅʜ'}"
    )
    buttons = [
        [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back_to_start")],
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]
    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/settings.jpg"),
        caption=await to_smallcaps(settings_text),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(client, callback_query):
    settings = get_settings()
    welcome_msg = settings["welcome_msg"]
    buttons = [
        [InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about")],
        [InlineKeyboardButton("sᴇᴛᴛɪɴɢs", callback_data="settings")]
    ]
    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/welcome.jpg"),
        caption=await to_smallcaps(welcome_msg),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("close"))
async def close_message(client, callback_query):
    await callback_query.message.delete()
