# вариант 12

import math

p = int(input("Задайте p:\n"))
x = -1


while True:
    y = pow(x, 3) + math.log10(7 * math.e) * p - 27
    print("{0} {1:.2f} {2} {3:.4f}".format("x =", x, "y(x) =", y))

    if x + p >= 7:
        y = pow((math.tan(p)) / (pow(x, 2) + 5 * x - 7), 2)
        print("{0} {1:.2f} {2} {3:.4f}".format("x =", x, "y(x) =", y))
        break
    
    x += 1