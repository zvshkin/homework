class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.name}")
        print(f"Тип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"Ресторан {self.name} открыт!\n")
