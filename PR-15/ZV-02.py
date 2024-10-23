from math import *

x = int(input("Задайте x:\n"))
y = int(input("Задайте y:\n"))

if x > 7 and y > 11:
    f = 4*sin(x)+5*y
elif x < 7 or 0 <= y <= 11:
    f = 2*pow(log(abs(x)),4)
else:
    f = pow(sqrt(pow(y,2)+pow(x,2)),3)

print("f = ", f)

file = open('lab15_1_out.txt', 'w')
file.write("F = " +str(f))
file.close()