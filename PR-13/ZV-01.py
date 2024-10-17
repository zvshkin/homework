import math
n = int(input("Введите число строк квадратной матрицы:\n"))
C = []
for i in range(n):
    C.append([])
    for j in range(n):
        C[i].append(math.sqrt(3*j+1)-math.log(i+2))

print("Сгенерированная матрица:")
for row in C:
    print(row)

C2 = []
for i in range(n):
    C2.append(C[i][1])
print("Эллементы воторого столбца:\n", C2)
min2 = min(C2)
print("Минимальный элемент второго столбца:\n", min2)

perv_row = 1
for b in C[0]:
    perv_row *= b
print("Произведение элементов первой строки:", perv_row)

proisv_pol = 1
for i in range(n):
    for j in range(n):
        if C[i][j] > 0:
            proisv_pol *= C[i][j]
print("Произведение положительных элементов матрицы C:", proisv_pol)

with open("lab13_1.txt", "w") as x:
    x.write("Сгенерированная матрица:\n")
    for row in C:
        x.write(str(row) + "\n")
    x.write("\nМинимальный элемент второго столбца:\n" + str(perv_row) + "\n")
    x.write("Произведение положительных элементов матрицы C:\n" + str(proisv_pol))
