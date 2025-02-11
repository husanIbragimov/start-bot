from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .states import NewStatement


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


async def new_statement_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Iltimos, ism-familiyangizni yuboring.")
    await state.set_state(NewStatement.name)


async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    the_state = await state.get_state()
    print(the_state)
    if the_state is None:
        await message.answer("Bekor qilish uchun joriy operatsiya yo'q.")
    else:
        await state.clear()
        await message.answer("Joriy operatsiyani bekor qildingiz.")


async def stop_command_answer_none_states(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Bekor qilish uchun joriy operatsiya yo'q.")


async def new_statement_name_answer(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 2:
        if message.text.split()[0].isalpha() and message.text.split()[1].isalpha():
            await state.update_data(name=message.text)
            await message.answer("Ism-familayngizni qabul qildim.")
            await message.answer("Yoshingizni yuboring. (masalan: 21)")
            await state.set_state(NewStatement.age)
        else:
            await message.answer("Ism-familiyada faqat harflar bo'lishi kerak.")
    else:
        await message.answer("Faqat ism-familiyangizni yuboring (masalan: John Doe).")


async def new_statement_age_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit() and 18 < int(message.text) < 100:
        await state.update_data(age=message.text)
        await message.answer("Yoshingizni qabul qildim.")
        await message.answer("Telefon raqamingizni yuboring.")
        await state.set_state(NewStatement.phone)
    elif int(message.text) < 18:
        await message.answer("Siz belgilangan yoshda emassiz.")
    else:
        await message.answer("Yoshingizni to'g'ri kiriting (masalan: 21).")


async def new_statement_phone_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(f"Telefon raqamingizni qabul qildim. \n\n{message.text}")
    await message.answer("Kasbingiz nima?")
    await state.set_state(NewStatement.job)


async def new_statement_job_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(f"Kasbingizni qabul qildim. \n\n{message.text}")
    await message.answer("Qanday maqsadda ?")
    await state.set_state(NewStatement.goal)


async def new_statement_goal_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(f"Maqsadingizni qabul qildim. \n\n{message.text}")
    await message.answer("Murojaatingiz qabul qilindi. Tez orada siz bilan bog'lanamiz.")
    data = await state.get_data()
    name = data.get('name')
    statement = (
        f"Ariza beruvchi: {message.from_user.mention_html(name)}\n"
        f"Yoshi: {data.get('age')}\n"
        f"Username: @{message.from_user.username}\n"
        f"Telefon raqami: {data.get('phone')}\n"
        f"Kasbi: {data.get('job')}\n"
        f"Maqsadi: {message.text}\n"
    )
    await message.answer(f"Arizani yuboraveraymi?\n\n{statement}\n\nHa(H) yoki yo'q(Y)?", parse_mode='HTML')
    await state.set_state(NewStatement.is_verify)


async def new_statement_is_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() in ['ha', 'h', 'yes', 'y', 'xa', 'x']:
        data = await state.get_data()
        name = data.get('name')
        statement = (
            f"Ariza beruvchi: {message.from_user.mention_html(name)}\n"
            f"Yoshi: {data.get('age')}\n"
            f"Username: @{message.from_user.username}\n"
            f"Link: {message.from_user.mention_html(f'{message.from_user.first_name}')}\n"
            f"Telefon raqami: {data.get('phone')}\n"
            f"Kasbi: {data.get('job')}\n"
            f"Maqsadi: {data.get('goal')}\n"
        )
        print(statement)
        await bot.send_message(663153232, f"Yangi ariza:\n\n{statement}", parse_mode='HTML')
        await message.answer("Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz.")
        await state.clear()
    else:
        await message.answer("Notog'ri komanda. Murojaatingizni qayta yuboring.")
