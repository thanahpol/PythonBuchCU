in_txt = input('Enter digits: ')
out_txt = ''
arabic = '0123456789'
thai   = '๐๑๒๓๔๕๖๗๘๙'

for d in in_txt :
    k = arabic.find(d)

    if k >= 0 :
        out_txt += thai[k]
    else :
        out_txt += d

print(out_txt)
