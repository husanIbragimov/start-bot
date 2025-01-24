from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import keys


async def echo(message: Message):
    await message.answer(message.text, reply_markup=keys.reply_keyboard)


async def cancel_markup(message: Message):
    await message.answer("Operation canceled", reply_markup=ReplyKeyboardRemove())
