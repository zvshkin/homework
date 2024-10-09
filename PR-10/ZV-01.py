import math

input_file = open('lab33.in', 'r')
x = float(input_file.readline())
a = float(input_file.readline())
z = float(input_file.readline())
input_file.close()

r = (pow(x,2)/pow(math.e,a)) + (1/5)*pow(math.sin(z),2) - math.log(math.sqrt(2*x))

output_file = open('lab33.out', 'w')
output_file.write('r = ' + str(r))
output_file.close()