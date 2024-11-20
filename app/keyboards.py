from gc import callbacks

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup)


# main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='регистрация')],
#                                     [KeyboardButton(text="FAQ")],
#                                     [KeyboardButton(text='Ваши заявки')]],
#                            resize_keyboard=True,
#                            input_field_placeholder="Выберите пункт меню...")

# Кнопки
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать новую заявку 📝"),
            KeyboardButton(text="Редактировать заявку ✏️"),
        ],
        {
            KeyboardButton(text="Профиль 👤"),
            KeyboardButton(text="FAQ ❔" ),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)

#inline кнопки
school_of_student = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text = "Студент",callback_data = 'student'),
        InlineKeyboardButton(text = "Школьник",callback_data = "school" )
    ]

    ]
)
