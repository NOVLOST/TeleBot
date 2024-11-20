from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


import app.keyboards as kb
import classes.client_class as cl


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    cl.client.full_name = message.from_user.full_name  # Полное имя пользователя

    await message.answer(f"Здравствуйте, {cl.client.full_name}\nЧем я могу вам помочь?", reply_markup=kb.start_keyboard)

@router.message(F.photo)
async def photo_handler(message: Message) -> None:
    photo_data = message.photo[0]
    photo_id = message.photo[0].file_id
    await message.answer(f"{photo_data}")  # получаем id файла(фотографии)
    # отправляем пользователю фотографию по id
    await message.answer_photo(photo=f'{photo_id}')


@router.message(F.text == 'FAQ ❔')
async def cmd_help(message: Message):
    await message.answer("Пройди короткую регистрацию для участия в конкурсе!")

#-------------------------------------
#РЕГИСТРАЦИЯ
#-------------------------------------

@router.message(F.text == "Создать новую заявку 📝")
async def registration(message: Message, state: FSMContext):
    await state.set_state(cl.client.real_first_name)
    await message.answer('Введите ваше имя')

@router.message(cl.client.real_first_name)
async def reg_real_first_name(message: Message, state: FSMContext):
    await state.update_data(real_first_name = message.text)
    print(cl.client.real_first_name)
    await state.set_state(cl.client.real_second_name)
    await message.answer("Введите вашу фамилию")

@router.message(cl.client.real_second_name)
async def reg_real_second_name(message: Message, state: FSMContext):
    await state.update_data(real_second_name = message.text)
    await state.set_state(cl.client.real_third_name)
    await message.answer("Введите ваше отчество")

@router.message(cl.client.real_third_name)
async def reg_real_third_name(message: Message, state: FSMContext):
    await state.update_data(real_third_name = message.text)
    await state.set_state(cl.client.school_or_student)
    await message.answer("Вы школьник или студент?",reply_markup=kb.school_of_student)

@router.message(F.data == 'student')
async def reg_student(callback: CallbackQuery, state: FSMContext):
    await state.update_data(school_or_student = 'student')
    print("stud")
    await state.set_state(cl.client.city)
    await callback.answer("Введите ваш город проживания")

@router.message(F.data == 'school')
async def reg_school(callback: CallbackQuery, state: FSMContext):
    await callback.answer('[jhjoj')
    await state.update_data(school_or_student = 'school')
    print("scholl")
    await state.set_state(cl.client.city)
    await callback.message.answer("Введите ваш город проживания")


