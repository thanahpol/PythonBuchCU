filename = input('Enter file name: ')

infile = open(filename, 'r')
outfile = open(filename + '_rot13.txt', 'w')


#line = input('Enter any text: ')

for line in infile :
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = upper.lower()

    upper2 = upper*2
    lower2 = lower*2
    rot13 = ''

    for c in line :
        if c in upper :
            k = upper.find(c)
            rot13 += upper2[k+13]

        elif c in lower :
            k = lower.find(c)
            rot13 += lower2[k+13]

        else :
            rot13 += c

    outfile.write(rot13)

#print('rot13 = ', rot13)

infile.close()
outfile.close()
