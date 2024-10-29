magicians = ["Leo", "Key", "Jay", "Ben", "Tom"]

def make_great(magicians):
    return ["Great " + mag for mag in magicians]

def show_magicians(magicians):
    for mag in magicians:
        print(mag)

print("Имена магов:")
show_magicians(magicians)

print("\nИмена магов с добавлением Great:")
great_magicians = make_great(magicians)
show_magicians(great_magicians)