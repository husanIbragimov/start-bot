from aiogram.types import Message
from aiogram import Bot
from keys import test_for_markup


async def start_command_reply(message: Message):
    await message.reply("Tugmalardan birini tanlang", reply_markup=test_for_markup)


async def get_contact(message: Message):

    await message.answer_contact("+998998989898", "Test", "Test")
    await message.answer_contact(message.contact.phone_number, message.contact.first_name, message.contact.last_name)


async def get_location(message: Message):
    await message.answer_location(41.2995, 69.2401)
    await message.answer_location(message.location.latitude, message.location.longitude)
