n = int(input('Enter the number of data: '))
data = []

for i in range(n) :
    x = float(input('>>'))
    data.append(x)
#--- --- --- --- -

sum = 0
for x in data :
    sum += x
avg = sum/n
#--- --- --- --- -

sum2 = 0
for x in data :
    sum2 += (x-avg)**2
sd = (sum2/n)**0.5
#--- --- --- --- -

print('average =', avg,',', 'standard deviation =', sd)
