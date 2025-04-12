from pyrogram import Client, filters
from config import ADMIN_IDS
from database import update_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("cst_welcome_msg") & filters.user(ADMIN_IDS))
async def custom_welcome_command(client, message):
    if len(message.command) < 2:
        await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ɴᴏᴛᴜɴ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇsᴇᴊ ᴅɪɴ!"))
        return

    new_welcome_msg = message.text.split(" ", 1)[1]
    update_settings({"welcome_msg": new_welcome_msg})
    await message.reply(await to_smallcaps("ᴡᴇʟᴄᴏᴍᴇ ᴍᴇsᴇᴊ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ!"))
