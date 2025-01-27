from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import users, get_user_ball
from states import Referral
from keys import main_menu


async def start_command(message: Message, state: FSMContext):
    print(message.text[7:])
    if message.text[7:].isdigit():
        if users.get(str(message.from_user.id)):
            if int(message.text[7:]) == message.from_user.id:
                await message.answer("Siz o'zingizga referal havola bera olmaysiz!")
            else:
                await message.answer("You already have a referral code!")
        else:
            refer_id = message.text[7:]
            users[str(message.from_user.id)] = {
                "refer_id": refer_id,
                "flag": False
            }
            print(users)
            await state.set_state(Referral.name)
            await message.answer("Ismingizni kiriting!")
    else:
        if users.get(str(message.from_user.id)):
            if users.get(str(message.from_user.id)).get("user_really_name"):
                await message.answer("Asosiy menyuga xush kelibsiz!", reply_markup=main_menu)
            else:
                await message.answer("Ism-familiyangizni kiriting!")
        else:
            users[str(message.from_user.id)] = {
                "refer_id": None,
                "flag": False
            }
            print(users)
            print(message.from_user.id)
            await state.set_state(Referral.name)
            await message.answer("Ismingizni kiriting!")


async def get_user_really_name(message: Message, state: FSMContext):
    users[str(message.from_user.id)]["user_really_name"] = message.text
    users[str(message.from_user.id)]["flag"] = True

    await message.answer(f"{message.text} sizni eslab qoldim.", reply_markup=main_menu)
    await state.clear()


async def get_referal_link(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        await message.answer(f"Sizning referal havolangiz: https://t.me/husandevbot?start={message.from_user.id}")
    else:
        users[str(message.from_user.id)] = {
            "refer_id": None,
            "flag": False
        }
        await state.set_state(Referral.name)
        await message.answer("Referal link olishdan oldin, Ismingizni kiriting!")


async def get_user_statistic(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        user_ball = get_user_ball(str(message.from_user.id))
        await message.answer(f"Sizning referal ballaringiz: {user_ball}")
    else:
        users[str(message.from_user.id)] = {
            "refer_id": None,
            "flag": False
        }
        await state.set_state(Referral.name)
        await message.answer("Referal link olishdan oldin, Ismingizni kiriting!")


