from telegram.ext import CommandHandler
from utils import get_all_users

def broadcast(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    if not context.args:
        update.message.reply_text("📢 Please provide a message.")
        return
    message = " ".join(context.args)
    users = get_all_users()
    for user_id in users:
        try:
            context.bot.send_message(chat_id=user_id, text=f"📢 **Broadcast**:\n{message}")
        except:
            continue
    update.message.reply_text("📢 **Broadcast Sent**!")

def setup_broadcast(dp):
    dp.add_handler(CommandHandler("broadcast", broadcast))
