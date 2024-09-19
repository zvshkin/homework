# вариант 12

import math

x = int(input("Задайте x:\n"))
p = int(input("Задайте p:\n"))

if x + p < 7:
    y = pow(x, 3) + math.log10(7*math.e) * p - 27
    print("Поскольку x =", x, ", а p =", p, ", то подходит условие: ", x, "+", p, "< 7")
    print("y =", y)

else:
    y = pow((math.tan(p))/(pow(x, 2) + 5*x - 7), 2)
    print("Поскольку x =", x, ", а p =", p, ", то подходит условие: ", x, "+", p, ">= 7")
    print("y =", y)