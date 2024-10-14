filename = 'reason.txt'

print("Введите 'стоп' для завершения программы.")

while True:
    reason = input("Почему вам нравится программировать? ")
    
    if reason.lower() == 'стоп':
        print("Выход из программы.")
        break
    
    with open(filename, 'a') as file:
        file.write("Причина:" + reason + "\n")
