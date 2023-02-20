#n = int(input('Enter the number of data: '))
#data = []

in_line = input('Enter data: ')
data = in_line.split()

#print('Number of data = ',len(data))
#print (in_line)
#print (data)

#data = in_line.split("w")
#print (data)

#x = " ".join(in_line)
#print (x)

#x = "--".join(in_line)
#print (x)

#for i in range(n) :
#    x = float(input('>>'))
#    data.append(x)
#--- --- --- --- -

sum = 0
for x in data :
    sum += float(x)
avg = sum/len(data)
#--- --- --- --- -

sum2 = 0
for x in data :
    sum2 += (float(x)-avg)**2
sd = (sum2/len(data))**0.5
#--- --- --- --- -

print('average =', avg,',', 'standard deviation =', sd)
