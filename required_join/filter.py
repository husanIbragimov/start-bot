from aiogram.types import Message
from aiogram.filters import Filter
from data import CHANNEL_ID
from aiogram import Bot


class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(CHANNEL_ID, message.from_user.id)
        if user_status.status in ["administrator", "member", "creator"]:
            return False
        return True

