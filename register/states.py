from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class SignUp(StatesGroup):
    name = State()
    age = State()

