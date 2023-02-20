infile = open('D:/Google Drive/__My Thumb/____Python/data.txt', 'r')

sum_score = 0
num_students = 0

for line in infile :
    num_students += 1
    score = float(line[10:])
    sum_score += score
    #ch_count += len(line)


#print('There are',l_count, 'lines and',ch_count, 'characters.')

infile.close()

avg = sum_score/num_students
print('Average = ', avg)
