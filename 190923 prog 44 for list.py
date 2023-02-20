x = [1,3,5,7,10]

for e in x :
    e *= 2
    print (e)

print('---')
#print('x has lenght =', len(x))
#print('---')

for i in range (0,len(x),2) :
    x[i] *= 2
    print(x[i])
