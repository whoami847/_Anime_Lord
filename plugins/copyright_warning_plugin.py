import asyncio
from pyrogram import Client, filters
from config import ADMIN_IDS
from database import get_settings, update_settings
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("cws") & filters.user(ADMIN_IDS))
async def copyright_warning_command(client, message):
    if len(message.command) < 2:
        await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ɴᴏᴛᴜɴ ᴄᴏᴘʏʀɪɢʜᴛ ᴡᴀʀɴɪɴɢ ᴍᴇsᴇᴊ ᴅɪɴ!"))
        return

    new_warning_msg = message.text.split(" ", 1)[1]
    update_settings({"copyright_warning_msg": new_warning_msg})
    await message.reply(await to_smallcaps("ᴄᴏᴘʏʀɪɢʜᴛ ᴡᴀʀɴɪɴɢ ᴍᴇsᴇᴊ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ!"))

async def apply_copyright_warning(client, message):
    settings = get_settings()
    warning_msg = settings["copyright_warning_msg"]
    warning_message = await message.reply(await to_smallcaps(warning_msg))

    # Auto-delete after 20 minutes (1200 seconds)
    await asyncio.sleep(1200)
    try:
        await warning_message.delete()
        await message.delete()
    except:
        pass
