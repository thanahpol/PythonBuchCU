i = int(input('Please insert total number? '))

sum = 0

for k in range(i):
    x = float(input('>> '))
    sum = sum + x

avg = sum/i

print(sum)
print('Average = ', avg)
