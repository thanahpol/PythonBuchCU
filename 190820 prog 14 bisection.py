a = float(input('a = '))

l = 0
u = a
x = (l+u)/2

while abs(x**2-a) > 1e-4:
    x = (l+u)/2
    if x**2 > a:
        u = x
    elif x**2 < a:
        l = x
    print(x, a**0.5)

print(x, a**0.5)
