from telegram.ext import CommandHandler
from plugins.forcesub import check_subscription

def auto_del(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    if context.args:
        try:
            new_time = int(context.args[0]) * 60  # Convert minutes to seconds
            context.bot_data["auto_delete_time"] = new_time
            update.message.reply_text(f"⏲️ **Auto Delete Time Set**: {context.args[0]} minutes")
        except ValueError:
            update.message.reply_text("⚠️ Please provide a number (in minutes).")
    else:
        current_time = context.bot_data.get("auto_delete_time", 20 * 60) // 60
        update.message.reply_text(f"⏲️ **Auto Delete Settings**:\nCurrent Time: {current_time} minutes")

def setup_auto_delete(dp):
    dp.add_handler(CommandHandler("auto_del", auto_del))
