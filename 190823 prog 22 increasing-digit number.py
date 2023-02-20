n = int(input('>> '))

is_increasing = True
right_of_d = 99

#print(n)

while is_increasing and  n != 0 :
    d = n%10
    n //= 10
    if d >= right_of_d :
        is_increasing = False
        break
    right_of_d = d

if is_increasing :
    print('Yes, this is an increasing-digit number')
else :
    print('No, this is not an increasing-digit number')

#print(n)
