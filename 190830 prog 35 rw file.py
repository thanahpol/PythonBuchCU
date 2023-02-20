src = input('Enter source file: ')
dest = input('Enter destination file name: ')

infile = open(src, 'r')
outfile = open(dest, 'w')

for line in infile :
    outfile.write(line)

infile.close()
outfile.close()
