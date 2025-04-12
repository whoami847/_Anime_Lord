import logging
from config import STORAGE_CHANNEL
from utils.storage import save_to_storage
from database import add_batch_file, clear_batch_files, get_batch_files
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def batch_command(client, message):
    logger.info(f"Received /batch command from user {message.from_user.id}")
    clear_batch_files()  # Clear previous batch
    await message.reply(await to_smallcaps("ʙᴀᴛᴄʜ ᴍᴏᴅᴇ sᴛᴀʀᴛᴇᴅ! sᴇɴᴅ ᴛʜᴇ ғɪʟᴇs ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏɴᴇ ʙʏ ᴏɴᴇ. ᴡʜᴇɴ ᴅᴏɴᴇ, ᴜsᴇ /ʙᴀᴛᴄʜ_ᴇɴᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs."))

async def batch_add_file(client, message):
    logger.info(f"Received batch_add_file command from user {message.from_user.id}")
    if not message.media:
        await message.reply(await to_smallcaps("ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ғɪʟᴇ ᴛᴏ ᴀᴅᴅ ᴛᴏ ᴛʜᴇ ʙᴀᴛᴄʜ!"))
        return

    file_message = await save_to_storage(client, message, STORAGE_CHANNEL)
    add_batch_file(file_message.id)
    await message.reply(await to_smallcaps("ғɪʟᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ʙᴀᴛᴄʜ! sᴇɴᴅ ᴛʜᴇ ɴᴇxᴛ ғɪʟᴇ ᴏʀ ᴜsᴇ /ʙᴀᴛᴄʜ_ᴇɴᴅ ᴛᴏ ғɪɴɪsʜ."))

async def batch_end_command(client, message):
    logger.info(f"Received /batch_end command from user {message.from_user.id}")
    batch_files = get_batch_files()
    if not batch_files:
        await message.reply(await to_smallcaps("ɴᴏ ғɪʟᴇs ᴡᴇʀᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ʙᴀᴛᴄʜ!"))
        return

    links = [
        f"https://t.me/c/{str(STORAGE_CHANNEL).replace('-100', '')}/{file_id}"
        for file_id in batch_files
    ]
    batch_links_text = await to_smallcaps("ʙᴀᴛᴄʜ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋs:\n\n" + "\n".join(links))
    await message.reply(batch_links_text)
    clear_batch_files()
