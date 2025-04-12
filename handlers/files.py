import logging
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def files_command(client, message):
    logger.info(f"Received /files command from user {message.from_user.id}")
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"))
        return

    settings = get_settings()
    protect_content_status = "ᴇɴᴀʙʟᴇᴅ" if settings["protect_content"] else "ᴅɪsᴀʙʟᴇᴅ"
    hide_caption_status = "ᴇɴᴀʙʟᴇᴅ" if settings["hide_caption"] else "ᴅɪsᴀʙʟᴇᴅ"
    channel_button_status = "ᴇɴᴀʙʟᴇᴅ" if settings["channel_button"] else "ᴅɪsᴀʙʟᴇᴅ"

    await message.reply(
        await to_smallcaps(
            f"📂 ғɪʟᴇ sᴇᴛᴛɪɴɢs\n\n"
            f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}\n"
            f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}\n"
            f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}\n\n"
            "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴛᴏɢɢʟᴇ:"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
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
                ]
            ]
        )
    )

async def toggle_protect_content(client, callback_query):
    logger.info(f"Received toggle_protect_content callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    settings = get_settings()
    settings["protect_content"] = not settings["protect_content"]
    update_settings(settings)

    protect_content_status = "ᴇɴᴀʙʟᴇᴅ" if settings["protect_content"] else "ᴅɪsᴀʙʟᴇᴅ"
    hide_caption_status = "ᴇɴᴀʙʟᴇᴅ" if settings["hide_caption"] else "ᴅɪsᴀʙʟᴇᴅ"
    channel_button_status = "ᴇɴᴀʙʟᴇᴅ" if settings["channel_button"] else "ᴅɪsᴀʙʟᴇᴅ"

    await callback_query.message.edit_text(
        await to_smallcaps(
            f"📂 ғɪʟᴇ sᴇᴛᴛɪɴɢs\n\n"
            f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}\n"
            f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}\n"
            f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}\n\n"
            "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴛᴏɢɢʟᴇ:"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
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
                ]
            ]
        )
    )
    await callback_query.answer()

async def toggle_hide_caption(client, callback_query):
    logger.info(f"Received toggle_hide_caption callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    settings = get_settings()
    settings["hide_caption"] = not settings["hide_caption"]
    update_settings(settings)

    protect_content_status = "ᴇɴᴀʙʟᴇᴅ" if settings["protect_content"] else "ᴅɪsᴀʙʟᴇᴅ"
    hide_caption_status = "ᴇɴᴀʙʟᴇᴅ" if settings["hide_caption"] else "ᴅɪsᴀʙʟᴇᴅ"
    channel_button_status = "ᴇɴᴀʙʟᴇᴅ" if settings["channel_button"] else "ᴅɪsᴀʙʟᴇᴅ"

    await callback_query.message.edit_text(
        await to_smallcaps(
            f"📂 ғɪʟᴇ sᴇᴛᴛɪɴɢs\n\n"
            f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}\n"
            f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}\n"
            f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}\n\n"
            "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴛᴏɢɢʟᴇ:"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
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
                ]
            ]
        )
    )
    await callback_query.answer()

async def toggle_channel_button(client, callback_query):
    logger.info(f"Received toggle_channel_button callback from user {callback_query.from_user.id}")
    if callback_query.from_user.id not in ADMIN_IDS:
        await callback_query.answer(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"), show_alert=True)
        return

    settings = get_settings()
    settings["channel_button"] = not settings["channel_button"]
    update_settings(settings)

    protect_content_status = "ᴇɴᴀʙʟᴇᴅ" if settings["protect_content"] else "ᴅɪsᴀʙʟᴇᴅ"
    hide_caption_status = "ᴇɴᴀʙʟᴇᴅ" if settings["hide_caption"] else "ᴅɪsᴀʙʟᴇᴅ"
    channel_button_status = "ᴇɴᴀʙʟᴇᴅ" if settings["channel_button"] else "ᴅɪsᴀʙʟᴇᴅ"

    await callback_query.message.edit_text(
        await to_smallcaps(
            f"📂 ғɪʟᴇ sᴇᴛᴛɪɴɢs\n\n"
            f"ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_content_status}\n"
            f"ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ: {hide_caption_status}\n"
            f"ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ: {channel_button_status}\n\n"
            "ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴛᴏɢɢʟᴇ:"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
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
                ]
            ]
        )
    )
    await callback_query.answer()
