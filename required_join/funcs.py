from aiogram.types import Message


async def get_channel_id(message: Message):
    return message.answer(f"Kanal ID'si: {message.forward_from_chat.id}")


async def echo(message: Message):
    return message.copy_to(message.chat.id)


async def alert_sub_channel(message: Message):
    invite_link = "https://t.me/+d4Wsi8dRYNUzZmUy"
    return message.answer(f"Kanal davet linki: <a href='{invite_link}'>havola</a>", parse_mode="HTML")
