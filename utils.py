import time
import pymongo
import os
import random
from pathlib import Path
from config import MONGO_URL

start_time = time.time()

# MongoDB initialization
def init_db():
    client = pymongo.MongoClient(MONGO_URL)
    db = client["anime"]
    return db

db = init_db()
users_collection = db["users"]

def add_user(user_id):
    users_collection.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

def get_user_count():
    return users_collection.count_documents({})

def get_all_users():
    users = users_collection.find({}, {"user_id": 1})
    return [user["user_id"] for user in users]

def get_uptime():
    uptime_seconds = int(time.time() - start_time)
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    return f"{hours} hours {minutes} minutes"

def get_random_image():
    # লোকাল ইমেজ ফোল্ডার থেকে ইমেজ লোড করা
    image_folder = Path("images")
    if image_folder.exists():
        images = list(image_folder.glob("*.jpg")) + list(image_folder.glob("*.png"))
        if images:
            return random.choice(images)
    return None
