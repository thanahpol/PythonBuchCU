n = int(input('Enter the number of data: '))
data = []

for i in range(n) :
    x = float(input('>>'))
    data.append(x)
#--- --- --- --- -
    
counts = [0]*n
for i in range (n) :
    for j in range (n) :
        if data[i] == data[j] :
            counts[i] += 1

maxI = 0

for i in range (n) :
    if counts[maxI] < counts[i] :
        maxI = i

print('mode =', data[maxI])
