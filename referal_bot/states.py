from aiogram.fsm.state import State, StatesGroup


class Referral(StatesGroup):
    name = State()
