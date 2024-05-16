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
        pass

    def add_user(self, username, userrights, email):
        # Проверка на заполненность всех аргументов и что они не пустые
        if not all([username.strip(), userrights.strip(), email.strip()]):
            return {'result': 'error0001', 'user': None}

        # Проверка на допустимые значения userrights
        if userrights not in ['user', 'admin']:
            return {'result': 'error0002', 'user': None}

        # Генерация уникального id для нового пользователя
        id = self.__gen_id_user()

        # Создание экземпляра класса USER
        new_user = USER(id, username, userrights, email)
        return {'result': 'done', 'user': new_user}

    def remove_user(self, id_user, sp_users):
        # Изменение статуса пользователя на неактивный
        find_result = self.__find_user(id_user, sp_users)
        if find_result['result'] == 'done':
            sp_users[find_result['index_sp_users']]._USER__active = False
            return {'result': 'done', 'sp_users': sp_users}
        else:
            return {'result': 'error0003', 'sp_users': sp_users}

    def __gen_id_user(self):
        # Формирование id на основе текущей даты, времени и тысячных долей секунды
        return int(datetime.now().strftime("%Y%m%d%H%M%S%f"))

    def __find_user(self, id_user, sp_users):
        # Поиск пользователя по id
        index_sp_users = -1
        for user in sp_users:
            index_sp_users += 1
            if user.get_user()['id'] == id_user:
                return {'result': 'done', 'index_sp_users': index_sp_users}
        return {'result': 'error0003', 'index_sp_users': None}


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

# Попытка добавить пользователя с пустым значением username
print("\nПопытка добавить пользователя с пустым значением username:")
result = admin.add_user(username='', userrights='user', email='test@example.com')
print(result['result'])

# Попытка добавить пользователя с недопустимым значением userrights
print("\nПопытка добавить пользователя с недопустимым значением userrights:")
result = admin.add_user(username=username, userrights='user11', email='test@example.com')
print(result['result'])

# Выполнение метода remove_user с id_user = 11 (если такой пользователь есть)
print("\nВыполнение метода remove_user с id_user = 11")
remove_result = admin.remove_user(11, USERS)
USERS = remove_result['sp_users']
print(remove_result)

# Вывод списка всех пользователей после удаления
print("\nСписок пользователей после удаления пользователя с id = 11:")
for user in USERS:
    print(user.get_user())

# Выполнение метода remove_user с id_user = id любого пользователя
if USERS:
    random_index = random.randint(0, 5)
    id_user = USERS[random_index].get_user()['id']
    print(f"\nУдаление пользователя с id = {id_user}:")
    remove_result = admin.remove_user(id_user, USERS)
    USERS = remove_result['sp_users']
    print(remove_result)

# Вывод списка всех пользователей после второго удаления
print("\nСписок пользователей после второго удаления:")
for user in USERS:
    print(user.get_user())
