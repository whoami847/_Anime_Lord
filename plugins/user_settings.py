from telegram.ext import CommandHandler
from plugins.forcesub import check_subscription
from utils import get_all_users

def users(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    users = get_all_users()
    if not users:
        update.message.reply_text("👤 **User List**:\nNo users found.")
        return
    user_list = "\n".join([f"User ID: {user}" for user in users])
    update.message.reply_text(f"👤 **User List**:\n{user_list}")

def setup_user_settings(dp):
    dp.add_handler(CommandHandler("users", users))
