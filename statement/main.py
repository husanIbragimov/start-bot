from asyncio import run

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import Command

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

from statement import states
from statement.funcs import (
    start_command_answer,
    help_command_answer,
    new_statement_answer,
    stop_command_answer,
    new_statement_name_answer,
    new_statement_age_answer, new_statement_phone_answer, new_statement_job_answer, new_statement_goal_answer,
    new_statement_is_verify_answer,
)

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
    dp.message.register(stop_command_answer, Command("stop", prefix="/!"))
    dp.message.register(new_statement_name_answer, states.NewStatement.name)
    dp.message.register(new_statement_age_answer, states.NewStatement.age)
    dp.message.register(new_statement_phone_answer, states.NewStatement.phone)
    dp.message.register(new_statement_job_answer, states.NewStatement.job)
    dp.message.register(new_statement_goal_answer, states.NewStatement.goal)
    dp.message.register(new_statement_is_verify_answer, states.NewStatement.is_verify)

    dp.shutdown.register(shutdown_answer)

    bot = Bot(token=BOT_TOKEN)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
        BotCommand(command="/new", description="Sent a new statement"),
        BotCommand(command="/stop", description="Cancel the current operation"),
    ])

    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    run(main())
