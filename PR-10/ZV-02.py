input_file = open('lab4_3.in', 'r')
q = float(input_file.readline())
input_file.close()

if (q < 4 or q >= 9) and q != 2.9:
    result = "Истинна", q, "принадлежит всей числовой оси, кроме интервала [4; 9) и числа 2.9"
else:
    result = "Ложь:", q, "не принадлежит допустимым интервалам"

output_file = open('lab4_3.out', 'w')
output_file.write(str(result))
output_file.close()
