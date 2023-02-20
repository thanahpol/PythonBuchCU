infile = open('D:/Google Drive/__My Thumb/____Python/data.txt', 'r')

min_score = 1000
max_score = 0
student = ''

#sum_score = 0
#num_students = 0

for line in infile :
    score = float(line[10:])
    student = line[0:10]
    
    if min_score > score :
        
        min_score = score
        min_student = student

    if max_score < score :
        
        max_score = score
        max_student = student

    #num_students += 1
    #score = float(line[10:])
    #sum_score += score
    #ch_count += len(line)


#print('There are',l_count, 'lines and',ch_count, 'characters.')

infile.close()

#avg = sum_score/num_students
print(min_student, 'get the minimum score at', min_score)
print(max_student, 'get the maximum score at', max_score)
