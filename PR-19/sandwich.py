def make_sandwich(*ingredients):
    print("Компоненты вашего сэндвича")
    for ingredient in ingredients:
        print("- " + str(ingredient))
    print()