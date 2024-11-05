num = [2, 7, 20, 21, 35, 40, 70]
print("Список до изменения:\n", num)
filtered = list(filter(lambda x: x % 7 != 0, num))
print("\nСписок после изменения:\n",filtered)