from pyrogram import Client, filters
from config import ADMIN_IDS
from database import get_all_users
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_IDS))
async def broadcast_command(client, message):
    if len(message.command) < 2:
        await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ᴇᴋᴛɪ ᴍᴇsᴇᴊ ᴅɪɴ!"))
        return

    broadcast_msg = message.text.split(" ", 1)[1]
    users = get_all_users()

    # Broadcast to all users
    for user_id in users:
        try:
            await client.send_message(user_id, await to_smallcaps(broadcast_msg))
        except:
            continue

    await message.reply(await to_smallcaps("ʙʀᴏᴀᴅᴄᴀsᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!"))
