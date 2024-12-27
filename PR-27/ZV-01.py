class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"Ресторан: {self.name}")
        print(f"Тип кухни: {self.type}")

    def open_restaurant(self):
        print(f"Ресторан {self.name} открыт!\n")


class IceCreamStand(Restaurant):

    def __init__(self, name, type="Мороженое"):
        super().__init__(name, type)
        self.flavors = []

    def set_flavors(self, flavors):
        self.flavors = flavors

    def show_flavors(self):
        print(f"Сорта мороженого в киоске '{self.name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")
        print()


ice_cream_stand = IceCreamStand("Морозко")

ice_cream_stand.set_flavors(["Шоколадное", "Ванильное", "Клубничное", "Фисташковое", "Карамельное"])

ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
