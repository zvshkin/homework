x = 7
y = 0

while True:
    z = int(input("Введите число:\n"))
    if x == z:
        print("Вы угадали число.")
        print("Вы потратили попыток: " + str(y))
        break
    else:
        print("Попробуйте другое число.")
        y += 1