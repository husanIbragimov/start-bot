from aiogram.fsm.state import State, StatesGroup


class NewStatement(StatesGroup):
    name = State()
    age = State()
    phone = State()
    job = State()
    goal = State()
