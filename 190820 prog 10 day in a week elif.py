
d = int(input('date = '))
m = int(input('number of month = '))
y = int(input('year = '))

if m < 3 :
    m += 12
    y -= 1

c = y // 100
k = y % 100
w = (d + 26*(m+1)//10 + k + k//4 + c//4 + 5*c) % 7

if w == 0 :
    print ("it's Saturday")

elif w == 1 :
    print ("it's Sunday")

elif w == 2 :
    print ("it's Monday")

elif w == 3 :
    print ("it's Tuesday")

elif w == 4 :
    print ("it's Wednesday")

elif w == 5 :
    print ("it's Thursday")

else :
    print ("it's Friday")
