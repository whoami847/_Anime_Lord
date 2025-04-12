import logging
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def help_command(client, message):
    logger.info(f"Received /help command from user {message.from_user.id}")
    help_text = await to_smallcaps(
        "📚 ʜᴇʟᴘ ᴍᴇɴᴜ\n\n"
        "ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:\n\n"
        "/sᴛᴀʀᴛ - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n"
        "/ʜᴇʟᴘ - sʜᴏᴡ ᴛʜɪs ʜᴇʟᴘ ᴍᴇɴᴜ\n"
        "/ғᴏʀᴄᴇsᴜʙ - ᴄʜᴇᴄᴋ ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ\n"
        "/ʀᴇǫ_ғsᴜʙ - ᴍᴀɴᴀɢᴇ ʀᴇǫᴜɪʀᴇᴅ ғᴏʀᴄᴇ sᴜʙ (ᴀᴅᴍɪɴ ᴏɴʟʏ)\n"
        "/ғɪʟᴇs - ᴍᴀɴᴀɢᴇ ғɪʟᴇ sᴇᴛᴛɪɴɢs (ᴀᴅᴍɪɴ ᴏɴʟʏ)\n"
        "/ᴀᴜᴛᴏ_ᴅᴇʟ - sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ (ᴀᴅᴍɪɴ ᴏɴʟʏ)\n"
        "/ɢᴇɴʟɪɴᴋ - ɢᴇɴᴇʀᴀᴛᴇ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n"
        "/ʙᴀᴛᴄʜ - sᴛᴀʀᴛ ʙᴀᴛᴄʜ ғɪʟᴇ sʜᴀʀɪɴɢ\n"
        "/ʙʀᴏᴀᴅᴄᴀsᴛ - ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ (ᴀᴅᴍɪɴ ᴏɴʟʏ)\n"
        "/ᴡᴇʟᴄᴏᴍᴇ_ᴍsɢ - sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ (ᴀᴅᴍɪɴ ᴏɴʟʏ)\n"
        "/ᴄᴡs - sᴇᴛ ᴄᴏᴘʏʀɪɢʜᴛ ᴡᴀʀɴɪɴɢ (ᴀᴅᴍɪɴ ᴏɴʟʏ)"
    )
    await message.reply(help_text)
