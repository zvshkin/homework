class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает {self.cuisine_type} кухню.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт для посетителей!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Перекрёсток", "русскую")
restaurant2 = Restaurant("Спар", "венгерскую")
restaurant3 = Restaurant("Чижик", "китайскую")

print("1.1\n")

print("Название ресторана:", restaurant.restaurant_name)
print("Тип кухни:", restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n1.2\n")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print("\n1.4\n")

print(f"Количество обслуженных посетителей: {restaurant.number_served}")

restaurant.number_served = 228
print(f"Количество обслуженных посетителей после изменения: {restaurant.number_served}")

restaurant.set_number_served(666)
print(f"Количество обслуженных посетителей после set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(334)
print(f"Количество обслуженных посетителей после increment_number_served(): {restaurant.number_served}")

print("\n1.3\n")

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"Профиль пользователя:\n"
              f"Имя: {self.first_name}\n"
              f"Фамилия: {self.last_name}\n"
              f"Возраст: {self.age}\n"
              f"Местоположение: {self.location}\n")

    def greet_user(self):
        print(f"Привет, {self.first_name} {self.last_name}! Добро пожаловать!\n")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Егор", "Кузнецов", 52, "Заволжье")
user2 = User("Михаил", "Литвин", 25, "Санкт-Петербург")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

print("1.5\n")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Количество попыток входа: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Количество попыток входа после сброса: {user1.login_attempts}")