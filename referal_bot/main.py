from asyncio import run

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import BotCommand
import funcs
import states

load_dotenv()


TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(663153232, "Hello, world!")


async def shutdown_answer(bot: Bot):
    await bot.send_message(663153232, "Goodbye, world!")


async def echo(message):
    await message.copy_to(message.chat.id)


async def main():
    dp.startup.register(startup_answer)

    dp.message.register(funcs.start_command, CommandStart())
    dp.message.register(funcs.get_user_really_name, states.Referral.name)
    dp.message.register(funcs.get_referal_link, F.text == "🔗 Referal havola")
    dp.message.register(funcs.get_user_statistic, F.text == "📊 Mening statistikam")

    dp.shutdown.register(shutdown_answer)

    bot = Bot(token=TOKEN)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
    ])

    await dp.start_polling(bot, polling_timeout=1)


if __name__ == '__main__':
      run(main())
