x = [1,3,5,7,11,13,17,19]

for e in x :
    print (e)

print('---')
print('x has lenght =', len(x))
print('---')

for i in range (0,len(x),2) :
    print(x[i])

print('---')
#print('x has lenght (negative) =', -len(x))

for i in range (-1,-len(x)-1,-1) :
    print(x[i])

print('---')

for i in range (len(x)-1,-1,-1) :
    print(x[i])
