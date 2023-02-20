
a = float (input('Enter coefficient a: ', ))
b = float (input('Enter coefficient b: ', ))
c = float (input('Enter coefficient c: ', ))

import math
x1 = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
x2 = (-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)

print('x = ', x1, 'and', x2)

s1 = a*(x1**2)+b*x1+c
s2 = a*(x2**2)+b*x2+c

print('s = ', s1, 'and', s2)
