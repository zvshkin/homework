filename = 'OP\PR-11\learning_python.txt'

with open(filename) as file:
    content = file.read()
    print(content)

with open(filename) as file:
    for line in file:
        print(line.strip())

with open(filename) as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())