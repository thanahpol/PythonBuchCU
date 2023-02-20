month = input('>> ').strip()

abbr = 'JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC'
k = abbr.find(month.upper())

#print(k)

if k < 0 :
    print('Invalid month abbreviation')
else :
    print(month, '-->', k//3+1)
