def count_lat(s):
    lat = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in lat:
            count += 1
    return count

s = "Hello World"

print("Количество гласных:", count_lat(s))
