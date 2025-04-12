import logging
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def custom_welcome_command(client, message):
    logger.info(f"Received /welcome_msg command from user {message.from_user.id}")
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"))
        return

    if len(message.command) < 2:
        settings = get_settings()
        current_msg = settings.get("welcome_msg", "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʙᴏᴛ!")
        await message.reply(
            await to_smallcaps(f"ᴄᴜʀʀᴇɴᴛ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ:\n\n{current_msg}\n\n"
                               "ᴛᴏ ᴜᴘᴅᴀᴛᴇ, ᴜsᴇ: /ᴡᴇʟᴄᴏᴍᴇ_ᴍsɢ <ɴᴇᴡ ᴍᴇssᴀɢᴇ>")
        )
        return

    new_welcome_msg = message.text.split(" ", 1)[1]
    update_settings({"welcome_msg": new_welcome_msg})
    await message.reply(await to_smallcaps("ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ!"))
