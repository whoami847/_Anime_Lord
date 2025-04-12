from telegram.ext import CommandHandler
from config import CHANNELS

def check_subscription(update, context):
    user_id = update.effective_user.id
    channels = context.bot_data.get("force_sub_channels", CHANNELS)
    for channel in channels:
        try:
            member = context.bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                update.message.reply_text(
                    f"⚠️ Sorry! You need to join {channel} first.\n"
                    "After joining, try again with /start"
                )
                return False
        except Exception as e:
            update.message.reply_text(f"⚠️ Error checking channel {channel}. Error: {str(e)}")
            return False
    return True

def forcesub(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    channels = context.bot_data.get("force_sub_channels", CHANNELS)
    update.message.reply_text(f"🔐 **Force Subscription Settings**:\nCurrently set channels:\n" + "\n".join(channels))

def req_fsub(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    if context.args:
        action = context.args[0].lower()
        if action == "add" and len(context.args) > 1:
            new_channel = context.args[1]
            if not new_channel.startswith("@"):
                update.message.reply_text("⚠️ Channel username must start with '@'.")
                return
            channels = context.bot_data.get("force_sub_channels", CHANNELS)
            if new_channel in channels:
                update.message.reply_text(f"⚠️ {new_channel} is already added.")
                return
            channels.append(new_channel)
            context.bot_data["force_sub_channels"] = channels
            update.message.reply_text(f"✅ {new_channel} has been set.")
        elif action == "remove" and len(context.args) > 1:
            channel_to_remove = context.args[1]
            channels = context.bot_data.get("force_sub_channels", CHANNELS)
            if channel_to_remove not in channels:
                update.message.reply_text(f"⚠️ {channel_to_remove} is not in the list.")
                return
            channels.remove(channel_to_remove)
            context.bot_data["force_sub_channels"] = channels
            update.message.reply_text(f"✅ {channel_to_remove} has been removed.")
        else:
            update.message.reply_text("📋 **Usage**:\n/req_fsub add @channel - Add a channel\n/req_fsub remove @channel - Remove a channel")
    else:
        channels = context.bot_data.get("force_sub_channels", CHANNELS)
        update.message.reply_text(f"📋 **Channels to Join**:\n" + "\n".join(channels))

def setup_forcesub(dp):
    dp.add_handler(CommandHandler("forcesub", forcesub))
    dp.add_handler(CommandHandler("req_fsub", req_fsub))
