# Roots of ax2 + bx + c = 0

a = float (input('Enter coefficient a: ', ))
b = float (input('Enter coefficient b: ', ))
c = float (input('Enter coefficient c: ', ))

import math

if a == 0:
    r = -c / b
    print ('root = ', r)
else:
    x1 = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = (-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)
    print('x = ', x1, 'and', x2)
    r1 = a*(x1**2)+b*x1+c
    r2 = a*(x2**2)+b*x2+c
    print('roots = ', r1, 'and', r2)
