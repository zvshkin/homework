x = int(input("Задайте x:\n"))
y = int(input("Задайте y:\n"))

if x > y:
    z = x-y
    print("x > y, они вычислились. Результат = " + str(z))

elif x < y:
    z = x+y
    print("x < y, они сложились. Результат = " + str(z))

else:
    z = x

print("Z = " + str(z))




# 2.6

mark = int(input("\n\n\nВведите желаемую оценку за практическую работу:\n"))

if mark == 5:
    print("Отлично!")

elif mark == 4:
    print("Хорошо!")

elif mark == 3:
    print("Удовлетворительно.")

elif mark == 2:
    print("Неудовлетворительно.")

else:
    print("Некорректная оценка.")