from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_settings, add_user
from plugins.smallcaps_plugin import to_smallcaps

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    # Add user to database
    add_user(message.from_user.id)

    # Get settings
    settings = get_settings()

    # Check force-sub
    if settings["request_fsub"]:
        for channel in settings["force_sub_channels"]:
            try:
                member = await client.get_chat_member(channel, message.from_user.id)
                if member.status not in ["member", "administrator", "creator"]:
                    await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ᴘʀᴏᴛʜᴏᴍᴇ ᴀᴍᴀᴅᴇʀ ᴄʜᴀɴᴇʟᴇ ᴊᴏʏᴇɴ ᴋᴏʀᴏ!"))
                    return
            except:
                await message.reply(await to_smallcaps("ᴅᴏʏᴀ ᴋᴏʀᴇ ᴘʀᴏᴛʜᴏᴍᴇ ᴀᴍᴀᴅᴇʀ ᴄʜᴀɴᴇʟᴇ ᴊᴏʏᴇɴ ᴋᴏʀᴏ!"))
                return

    # Send welcome message
    welcome_msg = settings["welcome_msg"]
    buttons = [
        [InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about")],
        [InlineKeyboardButton("sᴇᴛᴛɪɴɢs", callback_data="settings")]
    ]
    await message.reply_photo(
        photo="images/welcome.jpg",
        caption=await to_smallcaps(welcome_msg),
        reply_markup=InlineKeyboardMarkup(buttons)
                  )
