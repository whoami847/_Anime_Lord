import logging
from config import STORAGE_CHANNEL
from utils.storage import save_to_storage
from plugins.smallcaps_plugin import to_smallcaps
from plugins.copyright_warning_plugin import apply_copyright_warning

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def genlink_command(client, message):
    logger.info(f"Received /genlink command from user {message.from_user.id}")
    if not message.reply_to_message:
        logger.info("No reply-to message found for /genlink")
        await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ᴇᴋᴛɪ ғᴀɪʟ ᴘᴀᴛʜɪʏᴇ ᴛᴀʀ ʀᴇᴘʟʏ ᴅɪʏᴇ /ɢᴇɴʟɪɴᴋ ᴋᴏʀᴏ!"))
        return

    # Save file to storage channel
    logger.info("Saving file to storage channel...")
    file_message = await save_to_storage(client, message.reply_to_message, STORAGE_CHANNEL)

    # Generate link
    file_link = f"https://t.me/c/{str(STORAGE_CHANNEL).replace('-100', '')}/{file_message.id}"
    logger.info(f"Generated link: {file_link}")
    reply_message = await message.reply(await to_smallcaps(f"ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ: {file_link}"))

    # Apply copyright warning (temporarily commented out for debugging)
    # await apply_copyright_warning(client, reply_message)
