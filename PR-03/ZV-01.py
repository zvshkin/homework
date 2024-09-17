login = "Nikita"
password = "ZOV666"

login_input = input("Введите логин:\n")
password_input = input("Введите пароль:\n")

if login_input != login and password_input != password:
    print("Доступ запрещён - логин и пароль неверные!")

elif login_input != login:
    print("Неверный логин!")

elif password_input != password:
    print("Неверный пароль!")

if login_input == login and password_input == password:
    print("Успешная авторизация!")