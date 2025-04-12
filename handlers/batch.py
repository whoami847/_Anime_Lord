from pyrogram import Client, filters
from config import STORAGE_CHANNEL
from database import start_batch, add_to_batch, get_batch, clear_batch
from utils.storage import save_to_storage
from plugins.smallcaps_plugin import to_smallcaps
from plugins.copyright_warning_plugin import apply_copyright_warning

@Client.on_message(filters.command("batch") & filters.private)
async def batch_command(client, message):
    user_id = message.from_user.id
    batch_data = get_batch(user_id)

    if not batch_data:
        # Start a new batch
        start_batch(user_id)
        await message.reply(await to_smallcaps("ʙᴀᴛᴄʜ sᴛᴀʀᴛᴇᴅ! ғᴀɪʟ ᴘᴀᴛʜᴀɴ, ᴛᴀʀᴘᴏʀ ᴘᴜɴᴏʀᴀʏ /ʙᴀᴛᴄʜ ᴋᴏʀᴏ।"))
    else:
        # End the batch
        await batch_end_command(client, message)

@Client.on_message(filters.media & filters.private)
async def batch_add_file(client, message):
    user_id = message.from_user.id
    batch_data = get_batch(user_id)

    if batch_data:
        # Add file to batch
        add_to_batch(user_id, message.id)

async def batch_end_command(client, message):
    user_id = message.from_user.id
    batch_data = get_batch(user_id)

    if not batch_data or not batch_data["messages"]:
        await message.reply(await to_smallcaps("ᴋᴏɴᴏ ғᴀɪʟ ᴘᴀᴛʜᴀɴᴏ ʜᴀʏɴɪ!"))
        return

    # Save all files to storage channel
    message_ids = batch_data["messages"]
    saved_messages = []
    for msg_id in message_ids:
        msg = await client.get_messages(message.chat.id, msg_id)
        saved_msg = await save_to_storage(client, msg, STORAGE_CHANNEL)
        saved_messages.append(saved_msg.id)

    # Generate combo link
    start_id, end_id = min(saved_messages), max(saved_messages)
    combo_link = f"https://t.me/c/{str(STORAGE_CHANNEL).replace('-100', '')}/{start_id}-{end_id}"
    await message.reply(await to_smallcaps(f"ᴄᴏᴍʙᴏ ʟɪɴᴋ: {combo_link}"))

    # Clear batch
    clear_batch(user_id)

    # Apply copyright warning
    await apply_copyright_warning(client, message)
