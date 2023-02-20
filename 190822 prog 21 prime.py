n = int(input('Please define upperbound? '))

for k in range (2,n) :
    for m in range (2,k) :
        if k%m == 0 :
            break
    if m == k :
        print(k)
