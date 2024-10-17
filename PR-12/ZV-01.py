import math

C = []
for i in range(10):
    C_i = int(input("Задайте положительный элемент C[" + str(i) + "]: "))
    C.append(C_i)

a = int(input("Задайте число a: "))

Y = []
for i in range(10):
    Y_i = a**2 * math.sqrt(3 * C[i]) * pow(math.log(C[i]),2)
    Y.append(Y_i)

print("Массив Y:")
for i in range(10):
    print("Y[" + str(i) + "] = " + str(Y[i]))

max_y = max(Y)
print("Максимальный элемент Y:" + str(max_y))

bolshe5 = 0
for b in Y:
    if b > 5:
        bolshe5 += 1
print("Количество элементов > 5 : " + str(bolshe5))

with open("lab12_1.txt", "w") as f:
    f.write("Массив Y:\n")
    for i in range(10):
        f.write("Y[" + str(i) + "] = " + str(Y[i]) + "\n")
    f.write("Максимальный элемент Y : " + str(max_y) + "\n")
    f.write("Количество элементов > 5 :" + str(bolshe5) + "\n")
