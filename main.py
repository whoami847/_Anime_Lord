from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import start_command
from handlers.about import about_callback
from handlers.settings import settings_callback, back_to_start, close_message
from handlers.help import help_command
from handlers.forcesub import forcesub_command
from handlers.req_fsub import req_fsub_command
from handlers.files import files_command
from handlers.auto_del import auto_del_command
from handlers.genlink import genlink_command
from handlers.batch import batch_command, batch_end_command
from plugins.broadcast_plugin import broadcast_command
from plugins.custom_welcome_plugin import custom_welcome_command
from plugins.copyright_warning_plugin import copyright_warning_command, apply_copyright_warning
from plugins.smallcaps_plugin import to_smallcaps

# Pyrogram client
app = Client("AnimeLordBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Apply Sᴍᴀʟʟ Cᴀᴘs to all messages
async def apply_smallcaps(text):
    return to_smallcaps(text)

# Run the bot
if __name__ == "__main__":
    print("Aɴɪᴍᴇ Lᴏʀᴅ Bot is running...")
    app.run()
