import json
import re


def registration_system(user_fio, user_login, user_password):
    try:
        with open('./users.txt', encoding="UTF-8") as file:
                users = json.load(file)
    except:
        with open('./users.txt', 'w', encoding="UTF-8") as file:
            file.write("{}")
        with open('./users.txt', encoding="UTF-8") as file:
            users = json.load(file)

    len_user = len(users)
    i = 0
    while i < len_user:
        number = str(i)
        try:
            if user_login == users[number]['login']:
                return "Пользователь уже существует!"
        except KeyError:
            pass
        i += 1
    users.update({
        len_user: {
            'fio': user_fio,
            'login': user_login,
            'password': user_password,
            'is_admin': False,
            'check': []
        }
    })

    with open('./users.txt', 'w', encoding="UTF-8") as file:
        json.dump(users, file, ensure_ascii=False)

    return True


def authorisation_system(user_login, user_password):
    with open('./users.txt', encoding="UTF-8") as file:
        users = json.load(file)
        i = 0
        while i < len(users):
            number = str(i)
            try:
                if user_login == users[number]['login']:
                    if user_password == users[number]['password']:
                        return number
                    else:
                        return False
            except KeyError:
                pass
            i += 1
        else:
            return False


def adding_products(product_name, amount, price):
    with open('./products.txt', encoding="UTF-8") as file:
        products = json.load(file)
        id_product = len(products)
        products.update({
            id_product: {
                "product_name": product_name,
                "amount": amount,
                "price": price
            }
        })
    with open('./products.txt', 'w', encoding="UTF-8") as file:
        json.dump(products, file, ensure_ascii=False)
    return True


def buy_system(products=[]):
    lines = []
    for item in products:
        with open('./products.txt', encoding="UTF-8") as file:
            product = json.load(file)
            product_name = product[item]['product_name']
            amount = product[item]['amount']
            price = product[item]['price']
            product[item]['amount'] -= 1
            line = f'{product_name}: {price}₽'
            lines.append(line)
        with open('./products.txt', 'w', encoding="UTF-8") as file:
            json.dump(product, file, ensure_ascii=False)

    check = f"Чек за покупку:\n {lines}"
    print(check)


# registration_system(user_fio="Фамилия Имя Отчество", user_login="Логин", user_password="Пароль")
"""
Функция регистрации пользователя:
Как не трудно догадаться нужна для регистрации пользователя принимает 3 обязательных параметра:
user_fio - Принимает Фамилию Имя и Отчество пользователя, порядок слов при этом не важен(для карсаков не русский),
user_login - Принимает Логин пользователя. Проверяется на уникальность(2-х одинаковых не может быть). Если найден
            похожий, вернёт сообщение об ошибке,
user_password - Принимает пароль пользователя. Может быть каким угодно.
При удачной регистрации пользователя вернёт True.
"""
# authorisation_system(user_login="Логин", user_password="Пароль")
"""
Функция авторизации пользователя:
Авторизирует пользователя(вот это даа). Имеет следующие обязательные параметры:
user_login - Принимает Логин пользователя,
user_password - Принимает пароль пользователя.
При удачной авторизации пользователя вернёт number(id пользователя), в противном случае False.
"""
# adding_products(product_name="Ручки", amount=1500, price=15)
"""
Функция добавления товара:
Добавляет товары в список всех товаров. Имеет следующие обязательные параметры:
product_name - Принимает Название товара,
amount - Принимает Количество товара,
price - Принимает Цену товара(за штуку).
После добавление возвращает True.
"""
buy_system(products=['0', '0', '1'])
