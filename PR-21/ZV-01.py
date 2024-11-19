import math

def compute_population(t):
    C = 172
    T1 = 2000
    ti = 45
    return (C / ti) * math.atan((T1 - t) / ti)

line = input("Введите список лет через пробел: ")

years_str_list = line.split()

n = len(years_str_list)

years_list = [int(year) for year in years_str_list]

population_list = [compute_population(year) for year in years_list]

print("Результаты:")
for i in range(n):
    year = years_list[i]
    population = population_list[i]
    print("{:5d} - {:6.3f} миллиард(ов)".format(year, population))