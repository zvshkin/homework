import math

pi_const = round(math.pi, 2)

formula = lambda radius: pi_const * (radius ** 2)
radius = int(input("Задайте радиус круга: "))
ploshad = formula(radius)

print("Площадь круга с радиусом", radius, "=", ploshad)