# Commissioning 01
print(bool("George"))
print(bool(100))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()), '\n')

# Commissioning 02
html = 80
css = 60
javascript = 70
print((html > 50) and (css > 50) and (javascript > 50), '\n')

# Commissioning 03
num_one = 10
num_two = 20
num = 20
print((num > num_one) or (num > num_two))
print((num > num_one) and (num > num_two), '\n')

# Commissioning 04
num_one = 10
num_two = 20
result = 10 + 20
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000) / 5)
print(type(str(((result ** 3) % 26000) / 5)))