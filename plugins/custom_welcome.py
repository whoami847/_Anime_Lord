from telegram.ext import CommandHandler
from plugins.forcesub import check_subscription

def cst_welcome_msg(update, context):
    user_id = update.effective_user.id
    if user_id not in context.bot_data.get("admin_ids", []):
        update.message.reply_text("⚠️ Only admins can use this command!")
        return
    if context.args:
        action = context.args[0].lower()
        if action == "set" and len(context.args) > 1:
            new_msg = " ".join(context.args[1:])
            context.bot_data["welcome_message"] = new_msg
            update.message.reply_text(f"✅ **Welcome Message Set**:\n{new_msg}")
        elif action == "image" and len(context.args) > 1:
            if context.args[1].lower() == "add" and update.message.reply_to_message and update.message.reply_to_message.photo:
                image_id = update.message.reply_to_message.photo[-1].file_id
                if "welcome_images" not in context.bot_data:
                    context.bot_data["welcome_images"] = []
                context.bot_data["welcome_images"].append(image_id)
                update.message.reply_text("✅ **Welcome Image Added**! Total images: " + str(len(context.bot_data["welcome_images"])))
            elif context.args[1].lower() == "remove" and len(context.args) > 2:
                try:
                    index = int(context.args[2]) - 1
                    if "welcome_images" in context.bot_data and 0 <= index < len(context.bot_data["welcome_images"]):
                        removed_image = context.bot_data["welcome_images"].pop(index)
                        update.message.reply_text(f"✅ **Welcome Image Removed**! Total images: {len(context.bot_data['welcome_images'])}")
                    else:
                        update.message.reply_text("⚠️ Invalid image index or no images set.")
                except ValueError:
                    update.message.reply_text("⚠️ Please provide a valid number for the image index.")
            elif context.args[1].lower() == "list":
                if "welcome_images" in context.bot_data and context.bot_data["welcome_images"]:
                    update.message.reply_text(
                        f"📸 **Welcome Images List**:\nTotal images: {len(context.bot_data['welcome_images'])}\n"
                        "Use /cst_welcome_msg image remove <index> to remove an image."
                    )
                    for i, image_id in enumerate(context.bot_data["welcome_images"], 1):
                        update.message.reply_photo(photo=image_id, caption=f"Image {i}")
                else:
                    update.message.reply_text("⚠️ No welcome images are set.")
            else:
                update.message.reply_text(
                    "📋 **Usage**:\n"
                    "/cst_welcome_msg image add - Add an image (reply to a photo)\n"
                    "/cst_welcome_msg image remove <index> - Remove an image by index\n"
                    "/cst_welcome_msg image list - List all images"
                )
        else:
            update.message.reply_text(
                "📋 **Usage**:\n"
                "/cst_welcome_msg set <message> - Set welcome message\n"
                "/cst_welcome_msg image add - Add an image\n"
                "/cst_welcome_msg image remove <index> - Remove an image\n"
                "/cst_welcome_msg image list - List all images"
            )
    else:
        current_msg = context.bot_data.get("welcome_message", "🌟 Welcome, {user}!\nI am your file sharing bot.")
        total_images = len(context.bot_data.get("welcome_images", []))
        update.message.reply_text(f"✨ **Current Welcome Message**:\n{current_msg}\n📸 Total Images: {total_images}")

def setup_custom_welcome(dp):
    dp.add_handler(CommandHandler("cst_welcome_msg", cst_welcome_msg))
