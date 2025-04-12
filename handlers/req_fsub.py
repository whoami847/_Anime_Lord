import logging
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def req_fsub_command(client, message):
    logger.info(f"Received /req_fsub command from user {message.from_user.id}")
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"))
        return

    settings = get_settings()
    status = "ᴇɴᴀʙʟᴇᴅ" if settings["req_fsub"] else "ᴅɪsᴀʙʟᴇᴅ"
    await message.reply(
        await to_smallcaps(f"ʀᴇǫᴜɪʀᴇᴅ ғᴏʀᴄᴇ sᴜʙ ɪs ᴄᴜʀʀᴇɴᴛʟʏ {status}.\n\n"
                           "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴛᴏɢɢʟᴇ ɪᴛ:"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(await to_smallcaps("ᴇɴᴀʙʟᴇ"), callback_data="req_fsub_on"),
                    InlineKeyboardButton(await to_smallcaps("ᴅɪsᴀʙʟᴇ"), callback_data="req_fsub_off")
                ]
            ]
        )
    )

async def req_fsub_on(client, callback_query):
    logger.info(f"Received req_fsub_on callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    update_settings({"req_fsub": True})
    await callback_query.message.edit_text(
        await to_smallcaps("ʀᴇǫᴜɪʀᴇᴅ ғᴏʀᴄᴇ sᴜʙ ʜᴀs ʙᴇᴇɴ ᴇɴᴀʙʟᴇᴅ!"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(await to_smallcaps("ᴇɴᴀʙʟᴇ"), callback_data="req_fsub_on"),
                    InlineKeyboardButton(await to_smallcaps("ᴅɪsᴀʙʟᴇ"), callback_data="req_fsub_off")
                ]
            ]
        )
    )
    await callback_query.answer()

async def req_fsub_off(client, callback_query):
    logger.info(f"Received req_fsub_off callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    update_settings({"req_fsub": False})
    await callback_query.message.edit_text(
        await to_smallcaps("ʀᴇǫᴜɪʀᴇᴅ ғᴏʀᴄᴇ sᴜʙ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ!"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(await to_smallcaps("ᴇɴᴀʙʟᴇ"), callback_data="req_fsub_on"),
                    InlineKeyboardButton(await to_smallcaps("ᴅɪsᴀʙʟᴇ"), callback_data="req_fsub_off")
                ]
            ]
        )
    )
    await callback_query.answer()
