q = input("Блюдо 1: ")
w = input("Блюдо 2: ")
e = input("Блюдо 3: ")
r = input("Блюдо 4: ")
t = input("Блюдо 5: ")

y = (q,w,e,r,t,)

print("Меню ресторана:")
for z in y:
    print(z)


d = input("\nЗамените первое блюдо: ")
a = input("Замените второе блюдо: ")

b = (d,a,e,r,t,)

print("\nОбновлённое меню ресторана:")
for i in b:
    print(i)