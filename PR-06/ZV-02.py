# вариант 3

import math
import numpy

k1 = 1
k2 = 2

for c in numpy.arange(-3,5.1,0.4):
    if 2*pow(math.tan(c+k2),2) == 0: continue
    if (3*k1-c) < 0: continue
    f = math.sqrt(3*k1-c)/(2 * pow(math.tan(c+k2), 2))
    print("c =", "%.2f" % c, " f(x) =", "%.4f" % f)