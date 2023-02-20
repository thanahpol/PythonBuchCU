filename = input('Enter file name: ')

infile = open(filename, 'r')
outfile = open (filename + '_strip.txt', 'w')

for line in infile :
    line1 = line.strip()
    if len(line1) != 0 :
        outfile.write(line)


infile.close()
outfile.close()
