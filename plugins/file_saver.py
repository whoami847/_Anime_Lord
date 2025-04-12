from telegram.ext import CommandHandler, MessageHandler, Filters
from config import STORAGE_CHANNEL
from plugins.copyright_warning import start_copyright_timer
from plugins.forcesub import check_subscription

def genlink(update, context):
    if not check_subscription(update, context):
        return
    update.message.reply_text("📤 Please send a file, and I will save it and generate a link.")

def handle_file(update, context):
    if not check_subscription(update, context):
        return
    file = update.message.document or update.message.video or update.message.audio or update.message.photo
    if not file:
        update.message.reply_text("⚠️ Please send a file.")
        return
    try:
        forwarded_message = context.bot.forward_message(
            chat_id=STORAGE_CHANNEL,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )
        file_link = f"https://t.me/c/{STORAGE_CHANNEL.replace('-100', '')}/{forwarded_message.message_id}"
        context.bot_data.setdefault("file_links", {})[file_link] = forwarded_message.message_id
        update.message.reply_text(
            f"📁 **File Saved**!\nDownload Link: {file_link}\n"
            "⚠️ Copyright Warning: This file will be deleted after 20 minutes."
        )
        start_copyright_timer(context, STORAGE_CHANNEL, forwarded_message.message_id)
    except Exception as e:
        update.message.reply_text(f"⚠️ Error saving file: {str(e)}")

def handle_delete(update, context):
    if not update.message.reply_to_message:
        update.message.reply_text("⚠️ Please reply to the file link message.")
        return
    original_message = update.message.reply_to_message
    for link, message_id in context.bot_data.get("file_links", {}).items():
        if link in original_message.text:
            try:
                context.bot.delete_message(chat_id=STORAGE_CHANNEL, message_id=message_id)
                del context.bot_data["file_links"][link]
                update.message.reply_text("🗑️ **File Deleted**!")
            except:
                update.message.reply_text("⚠️ Error deleting file.")
            return
    update.message.reply_text("⚠️ File not found for this link.")

def setup_file_saver(dp):
    dp.add_handler(CommandHandler("genlink", genlink))
    dp.add_handler(MessageHandler(Filters.document | Filters.video | Filters.audio | Filters.photo, handle_file))
    dp.add_handler(MessageHandler(Filters.regex(r'^/delete$'), handle_delete))
