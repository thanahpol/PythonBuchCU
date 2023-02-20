import urllib.request

url = 'https://www.eng.chula.ac.th/th/news'
web = urllib.request.urlopen(url)

i = 1

for line in web :
    line = line.decode()

    if 'news-feed-title' in line :
        k = line.find('clamp2')
        k = line.find('>', k)
        j = line.find('</div>',k)

        print(i,')', line[k+1:j])
        i += 1
