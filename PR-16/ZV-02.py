print("\n2.1\n")

def make_sandwich(*ingredients):
    print("Компоненты вашего сэндвича")
    for ingredient in ingredients:
        print("- " + str(ingredient))
    print()

make_sandwich("сыр", "колбаса", "помидоры")
make_sandwich("курица", "майонез", "салат", "лук")
make_sandwich("бекон", "говядина", "сыр", "лук", "майонез")

print("\n2.2\n")

def build_profile(imya, fam, **info):
    print("Профиль студента:", imya, fam)
    for key, value in info.items():
        print("-", key, ":", value)

build_profile("Имя", "Фамилия", Возраст=" ", Город=" ", Группа=" ")

print("\n2.3\n")

def make_car(proisv, model, **info):
    car_info = {
        "Производитель": proisv,
        "Модель": model
    }
    car_info.update(info)
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)