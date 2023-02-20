import  math

tokens = input('>> ').split()

data = [math.sqrt(float(x)) for x in tokens if float(x) >= 0]

print(data)
