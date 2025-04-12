import logging
from config import ADMIN_IDS
from database import get_all_users
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def broadcast_command(client, message):
    logger.info(f"Received /broadcast command from user {message.from_user.id}")
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(await to_smallcaps("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs!"))
        return

    if not message.reply_to_message:
        await message.reply(await to_smallcaps("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ!"))
        return

    users = get_all_users()
    success_count = 0
    failed_count = 0

    for user_id in users:
        try:
            await message.reply_to_message.copy(user_id)
            success_count += 1
        except Exception:
            failed_count += 1

    await message.reply(
        await to_smallcaps(
            f"ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!\n\n"
            f"sᴜᴄᴄᴇss: {success_count}\n"
            f"ғᴀɪʟᴇᴅ: {failed_count}"
        )
    )
