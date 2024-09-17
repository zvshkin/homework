x = int(input("Задайте x:\n"))
y = int(input("Задайте y:\n"))

if x == y:
    result = x*y
    print("Т.к. x = y, они умножились. Произведение равно : " + str(result))

else:
    if x < y:
        result = x+y
        print("Т.к. x < y, они сложились. Сумма равна : " + str(result))
    else:
        x > y
        result = x-y
        print("Т.к. x > y, они вычислились. Разность равна : " + str(result))
