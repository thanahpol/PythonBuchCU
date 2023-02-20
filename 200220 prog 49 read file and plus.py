#infile = open('D:/Google Drive/__My Thumb/____Python/data1.txt')
infile = open('data4.txt')

sum = 0
for line in infile :
    line.strip()
    data = line.split()
    
    for x in data:
        sum += float(x)

#    print(line)
print(sum)

infile.close()
