import os
from asyncio import run

from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
from aiogram.filters import CommandStart

from required_join import funcs, filter

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def startup(bot: Bot):
    await bot.send_message(663153232, "Hello, world!")


async def shutdown(bot: Bot):
    await bot.send_message(663153232, "Goodbye, world!")


async def start():
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    dp.message.register(funcs.alert_sub_channel, filter.CheckSubChannel())
    dp.message.register(funcs.get_channel_id, F.forward_from_chat)
    dp.message.register(funcs.echo)

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    run(start())
