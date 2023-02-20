infile = open('test0903.txt')

x = list()
for line in infile :
    if line.strip() != 0 :
        x.append(float(line))
infile.close()

#--------------------------

sum = 0
sum1 = 0
n = len(x)

for e in x :
    sum += e
    sum1 += e**2
    
ave = sum/n
dev1 = sum1/n - ave**2

#--------------------------

sum2 = 0

for e in x :
    sum2 += (e-ave)**2

dev = sum2/n

print('Average = ', ave)
print('Deviation = ', dev)
print('Deviation1 = ', dev1)

#print('Average = ', ave, 'Deviation = ', dev, 'Deviation1 = ', dev1 )
