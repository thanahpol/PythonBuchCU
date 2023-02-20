# 29 days on Feb.

y = int(input('Input the number of year = '))
d = 28

if y%400==0 or y%4==0 and y%100!=0:
    d = 29

print('There are',d, 'days on the year',y)


