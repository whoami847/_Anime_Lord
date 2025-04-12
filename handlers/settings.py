import logging
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def settings_callback(client, callback_query):
    logger.info(f"Received settings callback from user {callback_query.from_user.id}")
    settings = get_settings()
    req_fsub_status = "ᴇɴᴀʙʟᴇᴅ" if settings["req_fsub"] else "ᴅɪsᴀʙʟᴇᴅ"
    protect_content_status = "ᴇɴᴀʙʟᴇᴅ" if settings["protect_content"] else "ᴅɪsᴀʙʟᴇᴅ"
    hide_caption_status = "ᴇɴᴀʙʟᴇᴅ" if settings["hide_caption"] else "ᴅɪsᴀʙʟᴇᴅ"
    channel_button_status = "ᴇɴᴀʙʟᴇᴅ" if settings["channel_button"] else "ᴅɪsᴀʙʟᴇᴅ"

    settings_text = await to_smallcaps(
        f"⚙️ ʙᴏᴛ sᴇᴛᴛɪɴɢs\n\n"
        f"ʀᴇǫᴜɪʀᴇᴅ ғᴏʀᴄᴇ sᴜʙ: {req_fsub_status}\n"
        f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}\n"
        f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}\n"
        f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}"
    )

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    await to_smallcaps(f"ʀᴇǫ ғᴏʀᴄᴇ sᴜʙ: {req_fsub_status}"),
                    callback_data="req_fsub_on" if not settings["req_fsub"] else "req_fsub_off"
                )
            ],
            [
                InlineKeyboardButton(
                    await to_smallcaps(f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}"),
                    callback_data="toggle_protect_content"
                )
            ],
            [
                InlineKeyboardButton(
                    await to_smallcaps(f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}"),
                    callback_data="toggle_hide_caption"
                )
            ],
            [
                InlineKeyboardButton(
                    await to_smallcaps(f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}"),
                    callback_data="toggle_channel_button"
                )
            ],
            [
                InlineKeyboardButton(await to_smallcaps("ʙᴀᴄᴋ"), callback_data="back_to_start"),
                InlineKeyboardButton(await to_smallcaps("ᴄʟᴏsᴇ"), callback_data="close")
            ]
        ]
    )

    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/settings.jpg"),
        caption=settings_text,
        reply_markup=reply_markup
    )
    await callback_query.answer()

async def back_to_start(client, callback_query):
    logger.info(f"Received back_to_start callback from user {callback_query.from_user.id}")
    welcome_text = await to_smallcaps(
        "ʜᴇʟʟᴏ! ɪ ᴀᴍ ᴀɴɪᴍᴇ ʟᴏʀᴅ ʙᴏᴛ.\n\n"
        "ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋs, ᴍᴀɴᴀɢᴇ ғɪʟᴇs, ᴀɴᴅ ᴍᴜᴄʜ ᴍᴏʀᴇ!"
    )

    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(await to_smallcaps("ᴀʙᴏᴜᴛ"), callback_data="about")],
            [InlineKeyboardButton(await to_smallcaps("sᴇᴛᴛɪɴɢs"), callback_data="settings")],
            [InlineKeyboardButton(await to_smallcaps("ᴄʟᴏsᴇ"), callback_data="close")]
        ]
    )

    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/welcome.jpg"),
        caption=welcome_text,
        reply_markup=reply_markup
    )
    await callback_query.answer()

async def close_message(client, callback_query):
    logger.info(f"Received close callback from user {callback_query.from_user.id}")
    await callback_query.message.delete()
    await callback_query.answer()
