from telegram.ext import CommandHandler
from plugins.forcesub import check_subscription

def cws(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    if context.args:
        new_msg = " ".join(context.args)
        context.bot_data["copyright_warning_message"] = new_msg
        update.message.reply_text(f"✅ **Copyright Warning Message Set**:\n{new_msg}")
    else:
        current_msg = context.bot_data.get("copyright_warning_message", "⚠️ Please forward this file within 20 minutes, otherwise it will be deleted.")
        update.message.reply_text(f"⚠️ **Current Copyright Warning Message**:\n{current_msg}")

def show_copyright_warning(context, update):
    warning_msg = context.bot_data.get("copyright_warning_message", "⚠️ Please forward this file within 20 minutes, otherwise it will be deleted.")
    update.message.reply_text(warning_msg)

def setup_copyright_message(dp):
    dp.add_handler(CommandHandler("cws", cws))
