from aiogram.fsm.state import State, StatesGroup


class AnswerToState(StatesGroup):
    user_id = State()
    message = State()
