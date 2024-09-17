number_1 = int(input("Введите первое число:\n"))
number_2 = int(input("Введите второе число:\n"))
oper = input("Введите знак операции (+, -, /, *, //, %):\n")

if oper == "+":
    result = number_1 + number_2
    print('Сумма = '+str(result))

elif oper == "-":
    result = number_1 - number_2
    print('Разность = '+str(result))

elif oper == "/":
    if number_2 == 0:
        print("Ошибка: деление на ноль невозможно!")
    else:
        result = number_1 / number_2
        print('Частное = '+str(result))

elif oper == "*":
    result = number_1 * number_2
    print('Произведение = '+str(result))

elif oper == "//":
    if number_2 == 0:
        print("Ошибка: деление на ноль невозможно!")
    else:
        result = number_1 // number_2
        print('Деление без остатка = '+str(result))

elif oper == "%":
    if number_2 == 0:
        print("Ошибка: деление на ноль невозможно!")
    else:
        result = number_1 % number_2
        print('Остаток от деления = '+str(result))

else:
    print("Ошибка: неверный знак операции! Пожалуйста, введите один из следующих знаков: +, -, /, *, //, %")