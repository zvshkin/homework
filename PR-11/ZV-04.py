with open('guest_book.txt', 'a') as file:
    while True:
        name = input("Пожалуйста, введите ваше имя (стоп, для завершения): ")

        if name.lower() == 'стоп':
            print("Спасибо за участие! До свидания!")
            break
        print("Здравствуй,", name)
        file.write(name + "\n")