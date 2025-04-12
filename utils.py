import time
import pymongo
import os
import random
from pathlib import Path
from config import MONGO_URL

start_time = time.time()

# MongoDB initialization
def init_db():
    try:
        client = pymongo.MongoClient(MONGO_URL)
        db = client["anime"]  # ডাটাবেস নাম ছোট হাতের অক্ষরে
        return db
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return None

db = init_db()
users_collection = db["users"] if db is not None else None  # এখানে 'if db' এর পরিবর্তে 'if db is not None' ব্যবহার করা হয়েছে

def add_user(user_id):
    if users_collection is None:
        print("MongoDB not connected. Skipping user addition.")
        return
    try:
        users_collection.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)
    except Exception as e:
        print(f"Error adding user to MongoDB: {e}")

def get_user_count():
    if users_collection is None:
        print("MongoDB not connected. Returning 0 for user count.")
        return 0
    try:
        return users_collection.count_documents({})
    except Exception as e:
        print(f"Error getting user count from MongoDB: {e}")
        return 0

def get_all_users():
    if users_collection is None:
        print("MongoDB not connected. Returning empty list for users.")
        return []
    try:
        users = users_collection.find({}, {"user_id": 1})
        return [user["user_id"] for user in users]
    except Exception as e:
        print(f"Error getting users from MongoDB: {e}")
        return []

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
