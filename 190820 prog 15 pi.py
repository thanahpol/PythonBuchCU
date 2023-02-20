import math

n = 22
d = 7
pi = math.pi

while abs(pi-n/d) >= 1e-8:

    nn = abs(pi-(n+1)/d)
    nd = abs(pi-n/(d+1))

    if nn < nd :
        n = n+1
    elif nd < nn :
        d = d+1

print('better valve is' ,n,'/',d)
