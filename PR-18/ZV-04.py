import math

cons_pi = round(math.pi, 2)

def conus_v(height, radius):
    return (height * cons_pi * (radius ** 2)) / 3
height = 10
radius = 5
v = conus_v(height, radius)
print("Объем конуса с высотой: " + str(height) + ", и радиусом: " + str(radius) + ", равен " + str(round(v, 2)))


conus_v_lambda = lambda height, radius: (height * cons_pi * (radius ** 2)) / 3
height = 10
radius = 5
v_lambda = conus_v_lambda(height, radius)
print("Объем конуса с высотой: " + str(height) + ", и радиусом: " + str(radius) + ", равен " + str(round(v_lambda, 2)))