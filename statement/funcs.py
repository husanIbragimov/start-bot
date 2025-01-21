from aiogram import Bot
from aiogram.types import Message

from statement.states import NewStatement


async def start_command_answer(message: Message, bot: Bot):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! bot bilan tanishin uchun /help buyrug'ini yuboring.")


async def help_command_answer(message: Message, bot: Bot):
    await message.answer("""
    Botdan foydalanish uchun quyidagi buyruqlardan foydalaning:\n
        /new - yangi murojaat yuboring\n
        /stop - joriy operatsiyani bekor qiling\n
        /help - yordam olish
    """)


async def new_statement_answer(message: Message, bot: Bot, state, FSMContext):
    await message.answer("Menga ism-familiyangizni yuboring.")
    await state.set_state(NewStatement.name)


async def stop_command_answer_in_states(message: Message, bot: Bot, state, FSMContext):
    await message.answer("Joriy operatsiyani bekor qildingiz.")
    await state.clear()


async def stop_command_answer_none_states(message: Message, bot: Bot, state, FSMContext):
    await message.answer("Bekor qilish uchun joriy operatsiya yo'q.")
