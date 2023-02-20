txt = input('>> ').lower()
start = txt.find('mailto:')
#stop = txt.find('"',start)
stop = txt.find('"',start)

print(txt[start+7:stop])
#print(stop)
