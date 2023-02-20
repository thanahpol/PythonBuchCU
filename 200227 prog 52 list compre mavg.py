
d = [float(x) for x in input('>> ').split()]

mavg = [d[i-1]+d[i]+d[i+1] for i in range(1,len(d)-1)]

mavg.insert(0, (d[0]+d[1])/2)
mavg.append( (d[-2]+d[-1])/2)


print(mavg)
