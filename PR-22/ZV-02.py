import numpy as np

with open("lab11_2.txt", 'r') as file:
    lines = file.readlines()
    
A = []
B = []
    
for line in lines:
    parts = line.split('=')
    chisla = list(map(float, parts[0].split()))
    rovno = float(parts[1].strip())

    """
    объяснение:
    
    в файле: 4.2 3.2 -4.2  8.5 = 13.2
    мы делим на две части | parts = line.split('=') | удаляя =
    
    4.2  3.2 -4.2  8.5 | первая часть [0]
    13.2               | вторая часть [1]

    parts[0].split() разбивает строку с числами на отдельные элементы, разделенные пробелами
    map(float, ...) преобразует каждую строку в число с точкой
    list(...) преобразует в список
    chisla = [4.2, 3.2, -4.2, 8.5]
    """
        
    A.append(chisla)
    B.append(rovno)
    
A = np.array(A)
B = np.array(B)
    
try:
    solution = np.linalg.solve(A, B)
except:
    solution = "Система не имеет единственного решения или не имеет решений."
    
with open("lab11_2_output.txt", 'w') as file:
    if type(solution) == str:
        file.write(solution)
    else:
        file.write("Решение системы: x1 = " + str(solution[0]) + 
           ", x2 = " + str(solution[1]) + 
           ", x3 = " + str(solution[2]) + 
           ", x4 = " + str(solution[3]) + "\n")
