x = 1
y = 2

# True
print((x == 1) and (y == 2))
print((x <= 2) and (y >= 1))
# False
print((y != 2) and (x <= 5))
print((x >= 2) and (y == 1))

# True
print((x >= y) or (y == 2))
print((y >= 2) or (x >= 5))
# False
print((2 != y) or (x <= 0))
print((x == 5) or (x != 1))


z = str("TG") 
v = str("VK")

# True
print((z != v) and (z == "TG"))
print((z != v) or (v == "INST"))
# False
print((v != z) and ("TG" == v))
print(("VK" == z)) or (z == "TG")