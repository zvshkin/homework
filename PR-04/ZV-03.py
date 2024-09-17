x = int(input("Задайте x:\n"))
y = int(input("Задайте y:\n"))

if (x > 5) and (4 < y < 5):
    f = 6*x+2*y

elif (0 < x <= 5) or (y <= 4):
    f = 3-x*y

else:
    f = y+x

print("F = " + str(f))