with open('OP\PR-11\learning_python.txt') as file:
    lines = file.readlines()
for line in lines:
    modified_line = line.replace('Python', 'Java')
    print(modified_line)