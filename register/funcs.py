from aiogram import Bot
from aiogram.types import Message
from states import SignUp
from aiogram.fsm.context import FSMContext


async def start_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.first_name}! Ismingizni kiriting", parse_mode="HTML")
    await state.set_state(SignUp.name)


async def help_answer(message: Message, bot: Bot):
    await message.answer(
        "Iltimos, quyidagi buyruqlardan foydalaning:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam"
    )


async def sign_up_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Ismingiz qabul qilindi: {message.text}")
    await message.answer("Yoshingizni kiriting:")
    await state.set_state(SignUp.age)


async def sign_up_age(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"""Ma'lumotlaringiz:
        Ismingiz: {data.get("name")}
        Yoshingiz: {message.text}
    """)
    await state.clear()
