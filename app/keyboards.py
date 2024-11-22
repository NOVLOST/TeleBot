
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup)




# Кнопки
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать новую заявку 📝"),
            KeyboardButton(text="Редактировать заявку ✏️"),
        ],
        [
            KeyboardButton(text="Профиль 👤"),
            KeyboardButton(text="FAQ ❔" ),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)


school_of_student = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text = "Студент"),
        KeyboardButton(text = "Школьник")
    ]

    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите один вариант"
)


get_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Отправить номер',request_contact=True )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="чтобы отправить номер нажните на кнопку"
)

choice_type_of_work = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Видео')
        ],
        [
            KeyboardButton(text = "Фото")
        ],
        [
            KeyboardButton(text = 'Другое')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите один из вариантов"
)
