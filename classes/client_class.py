from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class User(StatesGroup):

        real_first_name = State()
        real_second_name = State()
        real_third_name = State()
        school_or_student = State()
        city = State()
        education_place = State()
        phone_number = State()
        type_of_work = State()
        full_name = ""


client = User()