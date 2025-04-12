import logging
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def about_callback(client, callback_query):
    logger.info(f"Received about callback from user {callback_query.from_user.id}")
    about_text = await to_smallcaps(
        "ɪ ᴀᴍ ᴀɴɪᴍᴇ ʟᴏʀᴅ ʙᴏᴛ, ᴄʀᴇᴀᴛᴇᴅ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ᴀɴᴅ sʜᴀʀᴇ ғɪʟᴇs ᴇғғɪᴄɪᴇɴᴛʟʏ!\n\n"
        "✨ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs:\n"
        "- ɢᴇɴᴇʀᴀᴛᴇ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋs\n"
        "- ʙᴀᴛᴄʜ ғɪʟᴇ sʜᴀʀɪɴɢ\n"
        "- ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ sᴇᴛᴛɪɴɢs\n"
        "- ᴄᴏᴘʏʀɪɢʜᴛ ᴡᴀʀɴɪɴɢ sᴜᴘᴘᴏʀᴛ\n\n"
        "ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [ʏᴏᴜʀ ɴᴀᴍᴇ](https://t.me/your_username)"
    )

    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(await to_smallcaps("ʙᴀᴄᴋ"), callback_data="back_to_start")],
            [InlineKeyboardButton(await to_smallcaps("ᴄʟᴏsᴇ"), callback_data="close")]
        ]
    )

    await callback_query.message.edit_media(
        media=InputMediaPhoto("images/about.jpg"),
        caption=about_text,
        reply_markup=reply_markup
    )
    await callback_query.answer()
