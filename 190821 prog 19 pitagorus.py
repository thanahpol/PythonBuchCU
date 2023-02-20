x = 1
y = 1
z = 1

for x in range (1, 16):
    for y in range (1, 16):
        for z in range (1, 16):
            if z**2 == x**2+y**2 and x < y :
                print(str(x)+'^2 +', str(y)+'^2 =', str(z)+'^2')
                #print (x, y, z)
