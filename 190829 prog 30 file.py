infile = open('D:/Google Drive/__My Thumb/____Python/test.txt', 'r')

l_count = 0
ch_count = 0

for line in infile :
    l_count += 1
    ch_count += len(line)

print('There are',l_count, 'lines and',ch_count, 'characters.')

infile.close()
