import logging
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def auto_del_command(client, message):
    logger.info(f"Received /auto_del command from user {message.from_user.id}")
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"))
        return

    settings = get_settings()
    timer = settings.get("auto_delete_timer", 0)
    status = "ᴇɴᴀʙʟᴇᴅ" if timer > 0 else "ᴅɪsᴀʙʟᴇᴅ"
    timer_text = f"{timer // 60} ᴍɪɴᴜᴛᴇ(s)" if timer > 0 else "ɴᴏᴛ sᴇᴛ"

    await message.reply(
        await to_smallcaps(
            f"⏰ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ sᴇᴛᴛɪɴɢs\n\n"
            f"sᴛᴀᴛᴜs: {status}\n"
            f"ᴛɪᴍᴇʀ: {timer_text}\n\n"
            "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴍᴀɴᴀɢᴇ:"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(await to_smallcaps("sᴇᴛ ᴛɪᴍᴇʀ"), callback_data="set_timer"),
                    InlineKeyboardButton(await to_smallcaps("ᴅɪsᴀʙʟᴇ"), callback_data="disable_auto_delete")
                ]
            ]
        )
    )

async def disable_auto_delete(client, callback_query):
    logger.info(f"Received disable_auto_delete callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    update_settings({"auto_delete_timer": 0})
    await callback_query.message.edit_text(
        await to_smallcaps("⏰ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ!"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(await to_smallcaps("sᴇᴛ ᴛɪᴍᴇʀ"), callback_data="set_timer"),
                    InlineKeyboardButton(await to_smallcaps("ᴅɪsᴀʙʟᴇ"), callback_data="disable_auto_delete")
                ]
            ]
        )
    )
    await callback_query.answer()

async def set_timer(client, callback_query):
    logger.info(f"Received set_timer callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    # Placeholder for setting timer (requires user input handling)
    await callback_query.message.edit_text(
        await to_smallcaps("ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ᴛɪᴍᴇʀ ᴅᴜʀᴀᴛɪᴏɴ ɪɴ ᴍɪɴᴜᴛᴇs (ᴇ.ɢ., 5 ғᴏʀ 5 ᴍɪɴᴜᴛᴇs):")
    )
    await callback_query.answer()
