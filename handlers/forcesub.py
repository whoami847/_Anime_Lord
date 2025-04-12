import logging
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS
from database import get_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def forcesub_command(client, message):
    logger.info(f"Received /forcesub command from user {message.from_user.id}")
    settings = get_settings()
    if not settings["req_fsub"]:
        await message.reply(await to_smallcaps("ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴅɪsᴀʙʟᴇᴅ!"))
        return

    user_id = message.from_user.id
    not_subscribed = []

    for channel in CHANNELS:
        try:
            member = await client.get_chat_member(channel, user_id)
            if member.status not in ["member", "creator", "administrator"]:
                not_subscribed.append(channel)
        except Exception:
            not_subscribed.append(channel)

    if not_subscribed:
        buttons = [
            [InlineKeyboardButton(await to_smallcaps(f"ᴊᴏɪɴ {channel}"), url=f"https://t.me/{channel.lstrip('@')}")]
            for channel in not_subscribed
        ]
        buttons.append([InlineKeyboardButton(await to_smallcaps("ᴛʀʏ ᴀɢᴀɪɴ"), url=f"https://t.me/{client.me.username}?start=start")])
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(
            await to_smallcaps("ᴘʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄʜᴀɴɴᴇʟ(s) ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ:"),
            reply_markup=reply_markup
        )
    else:
        await message.reply(await to_smallcaps("ʏᴏᴜ ʜᴀᴠᴇ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs! ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ."))
