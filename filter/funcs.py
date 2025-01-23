from aiogram.types import Message


async def echo(message: Message):
    await message.copy_to(message.chat.id)
