#infile = open('D:/Google Drive/__My Thumb/____Python/data1.txt')
infile = open('data1.txt')

for line in infile :
    line.strip()

    print(line)

infile.close()
