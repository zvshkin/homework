x = input("Пожалуйста, введите ваше имя:\n")

with open('guest.txt', 'w') as file:
    file.write(x)

print("Ваше имя:", x, "сохранено в файле guest.txt.")