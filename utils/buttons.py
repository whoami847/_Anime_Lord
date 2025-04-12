from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_buttons(button_data):
    buttons = []
    for row in button_data:
        button_row = [InlineKeyboardButton(text, callback_data=callback) for text, callback in row]
        buttons.append(button_row)
    return InlineKeyboardMarkup(buttons)
