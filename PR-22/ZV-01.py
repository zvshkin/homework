# вариант 2

import numpy as np

n = int(input("Задайте размер матрицы M (n * n): "))

M = np.random.uniform(-4, 9, (n, n))

M_round = np.round(M, 3)

M_sum_otric = np.sum(M_round[M_round < 0])

M_max_odd = np.max(M_round[:, 1::2], axis=0) 
"""
[1:2:3] - срез, где 1 - начало, 2 - конец, 3 - шаг
[:, 1::2] - выбираем все строки (:) и столбцы с нечетными индексами (начиная с 1, с шагом 2)
axis=0 указывает, что нужно искать максимумы для каждого столбца отдельно (вдоль строк)
если axis не задан, NumPy вычисляет максимум для всех элементов массива как одного целого
"""
M_mean_max_odd = np.round(np.mean(M_max_odd), 3)

third_row = M_round[2, :]
M1 = np.zeros((n, n))
np.fill_diagonal(M1, third_row)

M_cos = np.cos(M_round)

M_odd = M[::2, :]

with open("lab11_1.txt", "w") as file:
    file.write("Размер матрицы: " + str(n) + " * " + str(n) + "\n")
    file.write("\nЗаполненная матрица M случайными числами:\n" + str(M) + "\n")
    file.write("\nОкруглённая матрица M (до тысячных):\n" + str(M_round) + "\n")
    if M_sum_otric == 0:
        file.write("\nВ матрице нет отрицательных чисел.\n")
    else:
        file.write("\nСумма отрицательных элементов: " + str(M_sum_otric) + "\n")
    file.write("\nМаксимальные элементы в нечётных столбцах:\n" + str(M_max_odd) + "\n")
    file.write("Их среднее арифметическое: " + str(M_mean_max_odd) + "\n")
    file.write("\nМатрица, главная диагональ которой - третья строка матрицы M:\n" + str(M1) + "\n")
    file.write("\nКосинусы каждого элемента матрицы M:\n" + str(M_cos) + "\n")
    file.write("\nПодматрица из нечётных строк матрицы M:\n" + str(M_odd) + "\n")

print("Вся информация записана в lab11_1.txt")