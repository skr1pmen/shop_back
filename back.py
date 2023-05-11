import json


def registration_system():
    user_fio = input("Введите своё ФИО:")  # Ввод пользовательской информации(в будущем поменять на переменные полей ввода)
    user_login = input("Введите логин:")  # Ввод пользовательской информации(в будущем поменять на переменные полей ввода)
    user_password = input("Введите пароль:")  # Ввод пользовательской информации(в будущем поменять на переменные полей ввода)

    try:
        with open('./users.txt', encoding="UTF-8") as file:
                users = json.load(file)
    except:
        with open('./users.txt', 'w', encoding="UTF-8") as file:
            file.write("{}")
        with open('./users.txt', encoding="UTF-8") as file:
            users = json.load(file)
    len_user = len(users)
    users.update({
        len_user: {
            'fio': user_fio,
            'login': user_login,
            'password': user_password,
            'is_admin': False,
            'check': []}
        }
    )

    with open('./users.txt', 'w', encoding="UTF-8") as file:
        json.dump(users, file)

    return True


def authorisation_system():
    user_login = input("Введите логин:")
    with open('./users.txt', encoding="UTF-8") as file:
        users = json.load(file)
        i = 0
        while i < len(users):
            number = str(i)
            try:
                if user_login == users[number]['login']:
                    user_password = input("Введите пароль:")
                    if user_password == users[number]['password']:
                        return True
                    else:
                        return False
            except KeyError:
                pass
            i += 1
        else:
            return False

# registration_system()
# authorisation_system()
