from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

test_for_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
