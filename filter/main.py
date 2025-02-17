import os
from asyncio import run

from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from filter import funcs
from filter.filters import IsExistsInText

load_dotenv()

TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


async def startup(bot: Bot):
    await bot.send_message(663153232, "Hello, world!")


async def shutdown(bot: Bot):
    await bot.send_message(663153232, "Goodbye, world!")


async def start():
    dp.startup.register(startup)
    dp.message.register(funcs.echo, IsExistsInText(["Salom", "Hello", "Привет"]))
    dp.shutdown.register(shutdown)

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    run(start())
