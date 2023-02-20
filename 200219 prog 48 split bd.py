
in_line = input('Enter Birthday (dd/mm/yyy): ')
data = in_line.split('/')

month_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', \
              'Oct','Nov','Dec']

month = month_name[int(data[1])-1]



#print('You were born on', data[0],'', month, '', data[2])
print('You were born on', data[0], month, data[2])
