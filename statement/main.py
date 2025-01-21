from asyncio import run

import environ
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import Command

from statement.funcs import start_command_answer, help_command_answer, new_statement_answer, \
    stop_command_answer_in_states

TOKEN = environ.Env().str("TOKEN")

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(663153232, "Hello, world!")


async def shutdown_answer(bot: Bot):
    await bot.send_message(663153232, "Goodbye, world!")


async def echo(message):
    await message.copy_to(message.chat.id)


async def main():
    dp.startup.register(startup_answer)

    dp.message.register(start_command_answer, Command("start", prefix="/!"))
    dp.message.register(help_command_answer, Command("help", prefix="/!"))
    dp.message.register(new_statement_answer, Command("new", prefix="/!"))
    dp.message.register(stop_command_answer_in_states, Command("stop", prefix="/!"))

    dp.shutdown.register(shutdown_answer)

    bot = Bot(token=TOKEN)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
        BotCommand(command="/new", description="Sent a new statement"),
        BotCommand(command="/stop", description="Cancel the current operation"),
    ])

    await dp.start_polling(bot, polling_timeout=1)


run(main())
