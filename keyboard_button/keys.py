from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

test_for_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
            KeyboardButton(text="Location", request_location=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Select an option",
)
