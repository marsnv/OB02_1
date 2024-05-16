from datetime import datetime
import random
import string
import time


class USER:
    def __init__(self, id, username, userrights, email):
        self.__id = id
        self.__username = username
        self.__userrights = userrights
        self.__email = email
        self.__active = True

    def get_user(self):
        # Возвращает все значения атрибутов пользователя
        return {
            'id': self.__id,
            'username': self.__username,
            'userrights': self.__userrights,
            'email': self.__email,
            'active': self.__active
        }


class ADMINUSER(USER):
    def __init__(self):
        # Список для хранения всех пользователей
        self.users = []

    def add_user(self, username, userrights, email):
        # Проверка на заполненность всех аргументов
        if not all([username, userrights, email]):
            return {'result': 'error0001', 'user': None}

        # Проверка на допустимые значения userrights
        if userrights not in ['user', 'admin']:
            return {'result': 'error0002', 'user': None}

        # Генерация уникального id для нового пользователя
        id = self.__gen_id_user()

        # Создание экземпляра класса USER
        new_user = USER(id, username, userrights, email)

        # Добавление нового пользователя в список
        self.users.append(new_user)

        return {'result': 'done', 'user': new_user}

    def remove_user(self, user):
        # Изменение статуса пользователя на неактивный
        if isinstance(user, USER):
            user_data = user.get_user()
            user_data['active'] = False
            return {'result': 'done', 'user': user}
        return {'result': 'error0003', 'user': None}

    def __gen_id_user(self):
        # Формирование id на основе текущей даты, времени и тысячных долей секунды
        return int(datetime.now().strftime("%Y%m%d%H%M%S%f"))

    def __find_user(self, id_user):
        # Поиск пользователя по id
        for user in self.users:
            if user.get_user()['id'] == id_user:
                return {'result': 'done', 'user': user}
        return {'result': 'error0003', 'user': None}


# Демонстрация работы программы
admin = ADMINUSER()

# Создание списка пользователей USERS
USERS = []

# Добавление трех пользователей с userrights = 'user'
for _ in range(3):
    time.sleep(0.3)
    username = ''.join(random.choices(string.ascii_lowercase, k=6))
    email = f"{username}@example.com"
    result = admin.add_user(username, 'user', email)
    if result['result'] == 'done':
        USERS.append(result['user'])

# Добавление трех пользователей с userrights = 'admin'
for _ in range(3):
    time.sleep(0.3)
    username = ''.join(random.choices(string.ascii_lowercase, k=6))
    email = f"{username}@example.com"
    result = admin.add_user(username, 'admin', email)
    if result['result'] == 'done':
        USERS.append(result['user'])

# Вывод списка всех пользователей
print("Список пользователей:")
for user in USERS:
    print(user.get_user())

# Выполнение метода remove_user с id_user = 11 (если такой пользователь есть)
print("\nУдаление пользователя с id = 11:")
find_result = admin._ADMINUSER__find_user(11)
if find_result['result'] == 'done':
    remove_result = admin.remove_user(find_result['user'])
    print(remove_result)
else:
    print(find_result)

# Вывод списка всех пользователей после удаления
print("\nСписок пользователей после удаления с id = 11:")
for user in USERS:
    print(user.get_user())

# Выполнение метода remove_user с id_user = id любого пользователя
if USERS:
    user_id = USERS[0].get_user()['id']
    print(f"\nУдаление пользователя с id = {user_id}:")
    find_result = admin._ADMINUSER__find_user(user_id)
    if find_result['result'] == 'done':
        remove_result = admin.remove_user(find_result['user'])
        print(remove_result)
    else:
        print(find_result)

# Вывод списка всех пользователей после второго удаления
print("\nСписок пользователей после второго удаления:")
for user in USERS:
    print(user.get_user())
