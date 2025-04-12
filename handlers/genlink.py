from pyrogram import Client, filters
from config import STORAGE_CHANNEL
from utils.storage import save_to_storage
from plugins.smallcaps_plugin import to_smallcaps
from plugins.copyright_warning_plugin import apply_copyright_warning

@Client.on_message(filters.command("genlink") & filters.private)
async def genlink_command(client, message):
    if not message.reply_to_message:
        await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ᴇᴋᴛɪ ғᴀɪʟ ᴘᴀᴛʜɪʏᴇ ᴛᴀʀ ʀᴇᴘʟʏ ᴅɪʏᴇ /ɢᴇɴʟɪɴᴋ ᴋᴏʀᴏ!"))
        return

    # Save file to storage channel
    file_message = await save_to_storage(client, message.reply_to_message, STORAGE_CHANNEL)

    # Generate link
    file_link = f"https://t.me/c/{str(STORAGE_CHANNEL).replace('-100', '')}/{file_message.id}"
    await message.reply(await to_smallcaps(f"ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ: {file_link}"))

    # Apply copyright warning
    await apply_copyright_warning(client, message)
