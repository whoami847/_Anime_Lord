from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.forcesub import check_subscription
from utils import get_user_count, get_uptime, add_user, get_random_image
from config import ADMIN_IDS

def start(update, context):
    if not check_subscription(update, context):
        return
    user = update.effective_user
    add_user(user.id)
    welcome_msg = context.bot_data.get("welcome_message", "🌟 Welcome, {user}!\nI am your file sharing bot.")
    welcome_msg = welcome_msg.format(user=user.first_name)
    
    # ইউজার অ্যাডমিন কিনা চেক করা
    is_admin = user.id in context.bot_data.get("admin_ids", [])
    
    # সাধারণ ইউজার এবং অ্যাডমিনদের জন্য মেনু তৈরি
    if is_admin:
        keyboard = [
            [
                InlineKeyboardButton("Generate Link", callback_data='genlink'),
                InlineKeyboardButton("Batch Save", callback_data='batch')
            ],
            [
                InlineKeyboardButton("Help", callback_data='help'),
                InlineKeyboardButton("Settings", callback_data='admin_settings')
            ],
            [
                InlineKeyboardButton("Broadcast", callback_data='broadcast'),
                InlineKeyboardButton("Restart", callback_data='restart')
            ],
            [
                InlineKeyboardButton("Set Welcome", callback_data='cst_welcome_msg'),
                InlineKeyboardButton("Set Copyright", callback_data='cws')
            ],
            [
                InlineKeyboardButton("Status", callback_data='status'),
                InlineKeyboardButton("Users", callback_data='users')
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("Generate Link", callback_data='genlink'),
                InlineKeyboardButton("Batch Save", callback_data='batch')
            ],
            [
                InlineKeyboardButton("Help", callback_data='help'),
                InlineKeyboardButton("About Me", callback_data='about')
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # প্রথমে টেলিগ্রাম সার্ভার থেকে ইমেজ লোড করার চেষ্টা
    if "welcome_images" in context.bot_data and context.bot_data["welcome_images"]:
        image_id = random.choice(context.bot_data["welcome_images"])
        update.message.reply_photo(
            photo=image_id,
            caption=welcome_msg,
            reply_markup=reply_markup
        )
    else:
        # যদি টেলিগ্রামে ইমেজ না থাকে, তাহলে লোকাল থেকে লোড করা
        image_path = get_random_image()
        if image_path:
            with open(image_path, 'rb') as photo:
                update.message.reply_photo(
                    photo=photo,
                    caption=welcome_msg,
                    reply_markup=reply_markup
                )
        else:
            update.message.reply_text(welcome_msg, reply_markup=reply_markup)

def menu(update, context):
    # /menu কমান্ডে একই মেনু দেখানো হবে
    if not check_subscription(update, context):
        return
    user = update.effective_user
    
    # ইউজার অ্যাডমিন কিনা চেক করা
    is_admin = user.id in context.bot_data.get("admin_ids", [])
    
    # সাধারণ ইউজার এবং অ্যাডমিনদের জন্য মেনু তৈরি
    if is_admin:
        keyboard = [
            [
                InlineKeyboardButton("Generate Link", callback_data='genlink'),
                InlineKeyboardButton("Batch Save", callback_data='batch')
            ],
            [
                InlineKeyboardButton("Help", callback_data='help'),
                InlineKeyboardButton("Settings", callback_data='admin_settings')
            ],
            [
                InlineKeyboardButton("Broadcast", callback_data='broadcast'),
                InlineKeyboardButton("Restart", callback_data='restart')
            ],
            [
                InlineKeyboardButton("Set Welcome", callback_data='cst_welcome_msg'),
                InlineKeyboardButton("Set Copyright", callback_data='cws')
            ],
            [
                InlineKeyboardButton("Status", callback_data='status'),
                InlineKeyboardButton("Users", callback_data='users')
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("Generate Link", callback_data='genlink'),
                InlineKeyboardButton("Batch Save", callback_data='batch')
            ],
            [
                InlineKeyboardButton("Help", callback_data='help'),
                InlineKeyboardButton("About Me", callback_data='about')
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("📋 **Menu**:\nChoose an option:", reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    is_admin = user_id in context.bot_data.get("admin_ids", [])
    
    if query.data == 'about':
        query.message.reply_text("🌟 This bot is designed for file sharing purposes.")
    elif query.data == 'help':
        if is_admin:
            help_text = (
                "📚 **Bot Usage Guide**:\n"
                "/start - Start the bot\n"
                "/menu - Show the menu\n"
                "/help - View this guide (admin)\n"
                "/status - View bot status (admin)\n"
                "/forcesub - View force subscription settings (admin)\n"
                "/req_fsub - View or edit required channels (admin)\n"
                "/genlink - Save a file and generate a link\n"
                "/batch - Save multiple files at once\n"
                "/auto_del - Set delete timer (admin)\n"
                "/users - View bot users list (admin)\n"
                "/broadcast - Send a message to all users (admin)\n"
                "/cst_welcome_msg - Customize welcome message (admin)\n"
                "/cws - Customize copyright warning message (admin)\n"
                "/cmd - View admin commands (admin)\n"
                "/restart - Restart the bot (admin)"
            )
            query.message.reply_text(help_text)
        else:
            query.message.reply_text(
                "📚 **Bot Usage Guide**:\n"
                "/start - Start the bot\n"
                "/menu - Show the menu\n"
                "/genlink - Save a file and generate a link\n"
                "/batch - Save multiple files at once"
            )
    elif query.data == 'genlink':
        query.message.reply_text("📤 Please send a file, and I will save it and generate a link.")
    elif query.data == 'batch':
        if "batch_files" not in context.user_data:
            context.user_data["batch_files"] = []
        if context.user_data["batch_files"]:
            from plugins.batch_save import batch
            batch(update, context)
        else:
            query.message.reply_text(
                "📦 Please send the files. When done, click 'Batch Save' again to finish."
            )
    elif query.data == 'admin_settings':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        query.message.reply_text("⚙️ **Admin Settings**:\n/req_fsub - Set force subscription\n/auto_del - Set delete timer")
    elif query.data == 'broadcast':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        query.message.reply_text("📢 Please provide a message to broadcast:\nExample: /broadcast Hello everyone!")
    elif query.data == 'restart':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        query.message.reply_text("🔄 Bot restarting...")
        import os
        os._exit(0)
    elif query.data == 'cst_welcome_msg':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        current_msg = context.bot_data.get("welcome_message", "🌟 Welcome, {user}!\nI am your file sharing bot.")
        total_images = len(context.bot_data.get("welcome_images", []))
        query.message.reply_text(
            f"✨ **Current Welcome Message**:\n{current_msg}\n📸 Total Images: {total_images}\n"
            "📋 **Usage**:\n"
            "/cst_welcome_msg set <message> - Set welcome message\n"
            "/cst_welcome_msg image add - Add an image\n"
            "/cst_welcome_msg image remove <index> - Remove an image\n"
            "/cst_welcome_msg image list - List all images"
        )
    elif query.data == 'cws':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        current_msg = context.bot_data.get("copyright_warning_message", "⚠️ Please forward this file within 20 minutes, otherwise it will be deleted.")
        query.message.reply_text(
            f"⚠️ **Current Copyright Warning Message**:\n{current_msg}\n"
            "📋 **Usage**:\n/cws <message> - Set a new copyright warning message"
        )
    elif query.data == 'status':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        user_count = get_user_count()
        uptime = get_uptime()
        query.message.reply_text(f"📊 **Bot Status**:\nTotal Users: {user_count}\nUptime: {uptime}")
    elif query.data == 'users':
        if not is_admin:
            query.message.reply_text("⚠️ Only admins can use this command!")
            return
        users = get_all_users()
        if not users:
            query.message.reply_text("👤 **User List**:\nNo users found.")
            return
        user_list = "\n".join([f"User ID: {user}" for user in users])
        query.message.reply_text(f"👤 **User List**:\n{user_list}")

def help_command(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    help_text = (
        "📚 **Bot Usage Guide**:\n"
        "/start - Start the bot\n"
        "/menu - Show the menu\n"
        "/help - View this guide (admin)\n"
        "/status - View bot status (admin)\n"
        "/forcesub - View force subscription settings (admin)\n"
        "/req_fsub - View or edit required channels (admin)\n"
        "/genlink - Save a file and generate a link\n"
        "/batch - Save multiple files at once\n"
        "/auto_del - Set delete timer (admin)\n"
        "/users - View bot users list (admin)\n"
        "/broadcast - Send a message to all users (admin)\n"
        "/cst_welcome_msg - Customize welcome message (admin)\n"
        "/cws - Customize copyright warning message (admin)\n"
        "/cmd - View admin commands (admin)\n"
        "/restart - Restart the bot (admin)"
    )
    update.message.reply_text(help_text)

def status(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    user_count = get_user_count()
    uptime = get_uptime()
    update.message.reply_text(f"📊 **Bot Status**:\nTotal Users: {user_count}\nUptime: {uptime}")

def cmd(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    cmd_text = (
        "🔧 **Admin Commands**:\n"
        "/cmd - View this list\n"
        "/restart - Restart the bot\n"
        "/broadcast - Send a message to all users\n"
        "/cst_welcome_msg - Customize welcome message\n"
        "/cws - Customize copyright warning message"
    )
    update.message.reply_text(cmd_text)

def restart(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    update.message.reply_text("🔄 Bot restarting...")
    import os
    os._exit(0)

def setup_handlers(dp):
    dp.bot_data["admin_ids"] = ADMIN_IDS
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("cmd", cmd))
    dp.add_handler(CommandHandler("restart", restart))
    dp.add_handler(CallbackQueryHandler(button_callback))
