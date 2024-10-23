from array import *
from math import *

A = array('f',range(0))
for i in range(10):
    A.append(float(input("Введи " +str(i)+ "-й элемент: ")))

b = int(input("Задайте b: "))

B = array('f',range(0))
for i in range(10):
    B.append(pow(sqrt(b + A[i]), 2) - pow(tan(A[i]), 2))

print("\nПолученный массив:")
for i in range(10):
    print("Элемент B[" + str(i) + "] равен: " + str(B[i]))

minmal = min(B)
print("\nМинимальный элемент масива B:", minmal)

min_index = B.index(min(B))
B[min_index], B[-1] = B[-1], B[min_index]
print("\nИзмененный массив:")
for i in range(10):
    print("Элемент B[" + str(i) + "] равен: " + str(B[i]))