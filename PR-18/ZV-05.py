def power(chislo, stepen):
    if stepen == 0:
        return 1
    elif stepen < 0:
        return 1 / pow(chislo, -stepen)
    else:
        return chislo * pow(chislo, stepen - 1)

number = int(input("Введите число: "))
exp = int(input("Введите степень: "))

result = pow(number, exp)

print(str(number) + " в степени " + str(exp) + ", равняется: " + str(result))