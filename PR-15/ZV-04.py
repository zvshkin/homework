A = [int(input(f"Введите элемент A[" + str(i) + "]: ")) for i in range(5)]
print()
B = [int(input(f"Введите элемент B[" + str(i) + "]: ")) for i in range(8)]

A.append(66)
print("Массив A после добавления 66: ", A)

B.pop(1)
print("Массив B после удаления второго элемента: ", B)

A.insert(2, 22)
print("Массив A после вставки 22 на третье место: ", A)

AB1 = A + B
print("Объединенный массив AB1: ", AB1)

AB1.sort(reverse=True)
print("Отсортированный массив AB1 по убыванию:", AB1)

AB2 = [AB1[i] for i in range(1, len(AB1), 2)]
print("Массив AB2 (элементы на четных местах):", AB2)

sdvig_AB2 = AB2[2:] + AB2[:2]
print("Массив AB2 после сдвига на 2 позиции влево: ", sdvig_AB2)

with open("lab15_3_out.txt", "w") as file:
    file.write("Массив A после добавления 66: " + str(A) + "\n")
    file.write("Массив B после удаления второго элемента: " + str(B) + "\n")
    file.write("Массив A после вставки 22 на третье место: " + str(A) + "\n")
    file.write("Объединенный массив AB1: " + str(AB1) + "\n")
    file.write("Отсортированный массив AB1 по убыванию: " + str(AB1) + "\n")
    file.write("Массив AB2 (элементы на четных местах): " + str(AB2) + "\n")
    file.write("Массив AB2 после сдвига на 2 позиции влево: " + str(sdvig_AB2) + "\n")
