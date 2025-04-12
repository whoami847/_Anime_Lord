from telegram.ext import CommandHandler, MessageHandler, Filters
from config import STORAGE_CHANNEL
from plugins.copyright_warning import start_copyright_timer
from plugins.forcesub import check_subscription

def batch(update, context):
    if not check_subscription(update, context):
        return
    if "batch_files" not in context.user_data:
        context.user_data["batch_files"] = []
    if context.user_data["batch_files"]:
        links = []
        for message_id in context.user_data["batch_files"]:
            try:
                forwarded_message = context.bot.forward_message(
                    chat_id=STORAGE_CHANNEL,
                    from_chat_id=update.message.chat_id,
                    message_id=message_id
                )
                file_link = f"https://t.me/c/{STORAGE_CHANNEL.replace('-100', '')}/{forwarded_message.message_id}"
                context.bot_data.setdefault("file_links", {})[file_link] = forwarded_message.message_id
                links.append(file_link)
                start_copyright_timer(context, STORAGE_CHANNEL, forwarded_message.message_id)
            except Exception as e:
                update.message.reply_text(f"⚠️ Error saving file: {str(e)}")
        context.user_data["batch_files"] = []
        update.message.reply_text(
            f"📦 **Batch Saved**!\nDownload Links:\n" + "\n".join(links) +
            "\n⚠️ Copyright Warning: These files will be deleted after 20 minutes."
        )
    else:
        update.message.reply_text(
            "📦 Please send the files. When done, use /batch again to finish."
        )

def handle_batch_file(update, context):
    if not check_subscription(update, context):
        return
    file = update.message.document or update.message.video or update.message.audio or update.message.photo
    if not file:
        return
    if "batch_files" not in context.user_data:
        context.user_data["batch_files"] = []
    context.user_data["batch_files"].append(update.message.message_id)

def setup_batch_save(dp):
    dp.add_handler(CommandHandler("batch", batch))
    dp.add_handler(MessageHandler(Filters.document | Filters.video | Filters.audio | Filters.photo, handle_batch_file))
