from aiogram.types import Message
from aiogram import Bot
from keys import test_for_markup


async def start_command_reply(message: Message):
    await message.reply("Tugmalardan birini tanlang", reply_markup=test_for_markup)


async def get_contact(message: Message):
    await message.reply("Kontakt tanlandi")
    contact_info = f"""
    {message}
    """
    print(contact_info)