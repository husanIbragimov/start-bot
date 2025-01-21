from asyncio import run

import environ
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import BotCommand

import states
from funcs import sign_up_name, sign_up_age, start_answer, help_answer

env = environ.Env()
environ.Env.read_env()

TOKEN = env.str('TOKEN')

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(663153232, "Hello, world!")


async def shutdown_answer(bot: Bot):
    await bot.send_message(663153232, "Goodbye, world!")


async def echo(message):
    await message.copy_to(message.chat.id)


async def main():
    dp.startup.register(startup_answer)

    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))
    dp.message.register(echo)
    dp.message.register(sign_up_name, states.SignUp.name)
    dp.message.register(sign_up_age, states.SignUp.age)

    dp.shutdown.register(shutdown_answer)

    bot = Bot(token=TOKEN)
    await bot.set_my_commands([
            BotCommand(command="/start", description="Start the bot"),
            BotCommand(command="/help", description="Get help"),
    ])

    await dp.start_polling(bot, polling_timeout=1)


run(main())
