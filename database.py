from pymongo import MongoClient
from config import MONGO_URL

# MongoDB client
mongo_client = MongoClient(MONGO_URL)
db = mongo_client["animelordbot_db"]
settings_collection = db["settings"]
users_collection = db["users"]
batch_collection = db["batch"]

# Default settings
default_settings = {
    "auto_delete": True,
    "delete_timer": 3600,  # 1 hour in seconds
    "protect_content": False,
    "hide_caption": True,
    "channel_button": True,
    "request_fsub": True,
    "force_sub_channels": [],
    "welcome_msg": "ʜᴇɪ, ᴀᴍɪ ᴇᴋᴛɪ ᴀᴅᴠᴀɴᴄᴇ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ। ᴀᴍᴀʀ sᴇʀᴀ ғɪᴄʜᴀʀ ʜᴏʟᴏ ᴀᴍɪ ʀᴇQᴜᴇsᴛ ғᴏʀᴄᴇ-sᴜʙ ғɪᴄʜᴀʀ sᴀᴘᴏʀᴛ ᴋᴏʀɪ, ʙɪsᴛᴀʀɪᴛ ᴊᴀɴᴛᴇ ᴋʟɪᴄᴋ ᴋᴏʀᴏ।",
    "copyright_warning_msg": "ғᴀɪʟ ғᴏʀᴡᴀʀᴅ ᴋᴏʀᴛᴇ ʜᴏʟᴇ 20 ᴍɪɴɪᴛᴇʀ ᴍᴏᴅʜʏᴇ ᴋᴏʀᴏ, ɴᴏɪʟᴇ ғᴀɪʟ ᴀᴜᴛᴏᴍᴇᴛɪᴋ ᴅɪʟɪᴛ ʜᴏʏᴇ ᴊᴀʙᴇ।",
    "banned_users": []
}

# Initialize settings if not exists
if not settings_collection.find_one():
    settings_collection.insert_one(default_settings)

# Functions to interact with the database
def get_settings():
    return settings_collection.find_one()

def update_settings(update_data):
    settings_collection.update_one({}, {"$set": update_data})

def add_user(user_id):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id})

def get_all_users():
    return [user["user_id"] for user in users_collection.find()]

def start_batch(user_id):
    batch_collection.insert_one({"user_id": user_id, "messages": []})

def add_to_batch(user_id, message_id):
    batch_collection.update_one({"user_id": user_id}, {"$push": {"messages": message_id}})

def get_batch(user_id):
    return batch_collection.find_one({"user_id": user_id})

def clear_batch(user_id):
    batch_collection.delete_one({"user_id": user_id})
