from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):

        real_first_name = State() #имя
        real_second_name = State() #фамилия
        real_third_name = State()# отчество
        school_or_student = State()#статус учашегося
        city = State() # город проживания
        education_place = State() # место обучения
        phone_number = State() #номер телефона
        type_of_work = State() # тип работы
        age = State() # возраст
        id_file = State() #мб удалим
        id_account = State()# id акка телеграм
        redux_mod = State()# вывод в чат всех заявок и выбор интересующей
        redux_mod_2 = State()# выбор пункта для редактирования заявки
        redux_mod_3 = State()# сохранение изменений и вывод об успешной операции
        num_of_photo = 0#счетчик номера фотографии
        num_of_bid = 0#счетчик номера заявки
        dict_redux_bid = {} #словарь для сохранения номеров заявок для редактирования
        #пользователь пишет номер это ключ для поиска нужной заявки
        download = State()


client = User()
