from threading import Thread
from config import AUTO_DELETE_TIME
from plugins.copyright_message import show_copyright_warning

def start_copyright_timer(context, chat_id, message_id):
    delay = context.bot_data.get("auto_delete_time", AUTO_DELETE_TIME)
    Thread(target=auto_delete, args=(context, chat_id, message_id, delay)).start()

def auto_delete(context, chat_id, message_id, delay):
    import time
    time.sleep(delay)
    try:
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        if "file_links" in context.bot_data and any(msg_id == message_id for link, msg_id in context.bot_data["file_links"].items()):
            for link, msg_id in list(context.bot_data["file_links"].items()):
                if msg_id == message_id:
                    del context.bot_data["file_links"][link]
    except:
        pass

def handle_forwarded_file(update, context):
    if update.message.forward_from_chat and update.message.forward_from_chat.id == int(STORAGE_CHANNEL.replace("-100", "")):
        message_id = update.message.forward_from_message_id
        if "file_links" in context.bot_data and any(msg_id == message_id for link, msg_id in context.bot_data["file_links"].items()):
            show_copyright_warning(context, update)

def setup_copyright_warning(dp):
    dp.add_handler(MessageHandler(Filters.forwarded, handle_forwarded_file))
