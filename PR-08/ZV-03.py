q = input("Задайте 1 строку: ")
w = input("Задайте 2 строку: ")
e = input("Задайте 3 строку: ")
r = input("Задайте 4 строку: ")

t = [q,w,e,r]
print("\n", t, "\n")

for z in t:
    for v in z:
        print(v, end="-")
    print()


f = list(input("\nСоздайте целочисленный список:"))
print(f)

for i in range(len(f)):
    f[i] = float(f[i])

print("\nСписок с числами с плавающей точкой:\n", f)