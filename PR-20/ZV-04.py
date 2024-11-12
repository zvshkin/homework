def read(file):
    try:
        with open(file, 'r') as f:
            print("\nСодержимое файла:", file)
            for line in f:
                print(str(" - ") + line.strip())
    except:
        pass

read("cats.txt")
read("dogs.txt")
read("dogss.txt")
