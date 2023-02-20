n = int(input('Number of loop: '))
s = 0
i = 1

while i != n+1:
    s += i**3
    i += 1

c = (n*(n+1)/2)**2
c = int(c)

print(i, s, c)
