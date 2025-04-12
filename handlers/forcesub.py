from pyrogram import Client, filters
from config import ADMIN_IDS
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("forcesub") & filters.user(ADMIN_IDS))
async def forcesub_command(client, message):
    forcesub_text = (
        "/ғsᴜʙ_ᴄʜɴʟ: ʙᴏʀᴛᴏᴍᴀɴ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴᴇʟ ᴄʜᴇᴄᴋ ᴋᴏʀᴏ (ᴀᴅᴍɪɴ)\n"
        "/ᴀᴅᴅ_ғsᴜʙ: ᴇᴋ ʙᴀ ᴇᴋᴀᴅʜɪᴋ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴᴇʟ ᴊᴏɢ ᴋᴏʀᴏ (ᴍᴀʟɪᴋ)\n"
        "/ᴅᴇʟ_ғsᴜʙ: ᴇᴋ ʙᴀ ᴇᴋᴀᴅʜɪᴋ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴᴇʟ ᴅɪʟɪᴛ ᴋᴏʀᴏ (ᴍᴀʟɪᴋ)"
    )
    await message.reply(await to_smallcaps(forcesub_text))
