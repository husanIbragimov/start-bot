from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No")
        ],
        [
            KeyboardButton(text="Cancel")
        ]
    ],
    resize_keyboard=True,
    # is_persistent=True,
    input_field_placeholder="Choose an options below 👇"
)
