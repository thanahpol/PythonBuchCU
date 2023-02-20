a = float(input('a = '))

x = 1

while x != a**0.5:
    x = (x+a/x)/2

print(x, a**0.5)
