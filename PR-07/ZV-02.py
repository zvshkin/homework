# вариант 2

while True:
    x = input("\nВведите строку:\n")

    if len(x) >= 20:

        # Для каждой буквы в строке x создается новый список, где каждая буква повторяется дважды
        # Затем объединяем этот список обратно в строку с помощью ''.join()
        x = ''.join([z * 2 for z in x]) 

        print("\nИзменённая строка выглядит так:")
        print(x)
        break

    else:
        print("\nВпишите строку длиной не менее 20 символов")
        continue