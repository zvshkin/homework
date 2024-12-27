class User:

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Профиль пользователя:\n"
              f"Имя: {self.first_name}\n"
              f"Фамилия: {self.last_name}\n"
              f"Возраст: {self.age}\n"
              f"Местоположение: {self.location}\n")


class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей"
        ]

    def show_privileges(self):
        print(f"Привилегии администратора {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()


admin = Admin("Аркадий", "Шваров", 52, "Городец")

admin.describe_user()
admin.show_privileges()
