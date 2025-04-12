import logging
from pyrogram import Client, filters
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    logger.info(f"Received /start command from user {message.from_user.id}")
    await message.reply(await to_smallcaps("ʜᴇʟʟᴏ! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀɴɪᴍᴇ ʟᴏʀᴅ ʙᴏᴛ."))
