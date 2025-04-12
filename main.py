import threading
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyrogram import Client, filters  # Ensure 'filters' is imported
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import start_command
from handlers.about import about_callback
from handlers.settings import settings_callback, back_to_start, close_message
from handlers.help import help_command
from handlers.forcesub import forcesub_command
from handlers.req_fsub import req_fsub_command, req_fsub_on, req_fsub_off
from handlers.files import files_command, toggle_protect_content, toggle_hide_caption, toggle_channel_button
from handlers.auto_del import auto_del_command, disable_auto_delete, set_timer
from handlers.genlink import genlink_command
from handlers.batch import batch_command, batch_end_command, batch_add_file
from plugins.broadcast_plugin import broadcast_command
from plugins.custom_welcome_plugin import custom_welcome_command
from plugins.copyright_warning_plugin import copyright_warning_command, apply_copyright_warning
from plugins.smallcaps_plugin import to_smallcaps

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Pyrogram client
app = Client("AnimeLordBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Apply Sᴍᴀʟʟ Cᴀᴘs to all messages
async def apply_smallcaps(text):
    return to_smallcaps(text)

# Define a simple HTTP server for health checks
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Anime Lord Bot is running!")  # Use ASCII characters only

def run_health_check_server():
    server_address = ("", 8080)  # Listen on port 8080
    httpd = HTTPServer(server_address, HealthCheckHandler)
    logger.info("Starting health check server on port 8080...")
    httpd.serve_forever()

# Register callback query handlers
app.on_callback_query(filters.regex("about"))(about_callback)
app.on_callback_query(filters.regex("settings"))(settings_callback)
app.on_callback_query(filters.regex("back_to_start"))(back_to_start)
app.on_callback_query(filters.regex("close"))(close_message)
app.on_callback_query(filters.regex("req_fsub_on"))(req_fsub_on)
app.on_callback_query(filters.regex("req_fsub_off"))(req_fsub_off)
app.on_callback_query(filters.regex("toggle_protect_content"))(toggle_protect_content)
app.on_callback_query(filters.regex("toggle_hide_caption"))(toggle_hide_caption)
app.on_callback_query(filters.regex("toggle_channel_button"))(toggle_channel_button)
app.on_callback_query(filters.regex("disable_auto_delete"))(disable_auto_delete)
app.on_callback_query(filters.regex("set_timer"))(set_timer)

# Run the health check server in a separate thread
if __name__ == "__main__":
    # Start the health check server in a separate thread
    health_check_thread = threading.Thread(target=run_health_check_server, daemon=True)
    health_check_thread.start()

    # Start the Pyrogram bot
    logger.info("Aɴɪᴍᴇ Lᴏʀᴅ Bot is running...")
    app.run()
