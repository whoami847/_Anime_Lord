from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    help_text = "ʜᴀʟʟᴏ, ᴀᴍɪ ᴇᴋᴛɪ ᴘʀᴀɪᴠᴇᴛ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ, ɴɪʀᴅɪsʜᴛᴏ ᴄʜᴀɴᴇʟᴇʀ ᴊᴏɴʏᴏ ғɪʟᴇ ᴏ ᴘʀᴏʏᴏᴊᴏɴɪʏᴏ ᴊɪɴɪs sᴘᴇsʜᴀʟ ʟɪɴᴋᴇʀ ᴍᴀᴅʜʏᴏᴍᴇ ᴅᴇᴏʏᴀʀ ᴊᴏɴʏᴏ ᴛᴏɪʀɪ। ᴇᴋʜᴏɴᴏ sᴏɴᴅᴇʜ ᴀᴄʜᴇ? ɴɪᴄʜᴇʀ ʙʏᴀᴋᴛɪ/ɢʀᴜᴘᴇʀ sᴀᴛʜᴇ ᴊᴏɢᴀᴊᴏɢ ᴋᴏʀᴏ!"
    buttons = [
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ɢʀᴏᴜᴘ", url="your_support_group_link")],
        [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="your_owner_link")],
        [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/shidoteshika1")]
    ]
    await message.reply_photo(
        photo="images/help.jpg",
        caption=await to_smallcaps(help_text),
        reply_markup=InlineKeyboardMarkup(buttons)
    )
