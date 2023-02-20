infile = open('test0903.txt')

sum = 0
n = 0

for line in infile :
    sum += float(line)
    n += 1

infile.close()

ave = sum/n

infile = open('test0903.txt')

sum2 = 0
#n = 0

for line in infile :
    sum2 += (float(line)-ave)**2
    #n += 1

infile.close()

dev = sum2/n

print('Average = ', ave,
      'Deviation = ', dev)
