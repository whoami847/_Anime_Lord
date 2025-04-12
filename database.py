import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# In-memory storage for settings (temporary, without MongoDB)
default_settings = {
    "req_fsub": False,
    "protect_content": False,
    "hide_caption": False,
    "channel_button": False,
    "auto_delete_timer": 0,
    "welcome_msg": "Welcome to the bot!",
    "copyright_warning_msg": "⚠️ This file is copyrighted. Do not share without permission!"
}
settings = default_settings.copy()

# In-memory storage for users (temporary, without MongoDB)
users = set()

# In-memory storage for batch files (temporary, without MongoDB)
batch_files = []

def get_settings():
    logger.info("Fetching settings from in-memory storage")
    return settings

def update_settings(new_settings):
    logger.info(f"Updating settings: {new_settings}")
    settings.update(new_settings)

def get_all_users():
    logger.info("Fetching all users from in-memory storage")
    return users

def add_user(user_id):
    logger.info(f"Adding user {user_id} to in-memory storage")
    users.add(user_id)

# Batch file management functions
def add_batch_file(file_id):
    logger.info(f"Adding batch file {file_id} to in-memory storage")
    batch_files.append(file_id)

def clear_batch_files():
    logger.info("Clearing batch files from in-memory storage")
    batch_files.clear()

def get_batch_files():
    logger.info("Fetching batch files from in-memory storage")
    return batch_files
