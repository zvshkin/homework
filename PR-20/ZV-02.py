while True:
    try:
        x = int(input("Введите первое число: "))
        break
    except:
        print("\nОшибки: Впишите целое число.\n")

while True:
    try:
        y = int(input("Введите второе число: "))
        print("Сумма 2-ух чисел =", x+y)
        break
    except:
        print("\nОшибка: Впишите целое число.\n")
