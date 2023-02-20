
data = []

for x in range(0,2001,2):
    data.append(x)

print(data[0])
print(data[999])
print(data[1000])        

data1 = [2*y for y in range(0,2001,2)]

print(data1[0])
print(data1[999])
print(data1[1000])

data2 = [z for z in range(0,2001) if z%2 == 0]

print(data2[0])
print(data2[999])
print(data2[1000])
