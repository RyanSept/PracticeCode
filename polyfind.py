##def polyfind(n):
##    angles=(n-2)*180
##    single_angle=angles/n
##    print "Sides: "+str(n),"Sum of interior angles: "+str(angles),"Size of single angle: "+str(single_angle)
##    n = n+1
##    print (n-2)*180/n-single_angle
##for i in range(2,41):
##    polyfind(i)
import urllib2,urllib
from bs4 import BeautifulSoup
import os
link="http://192.168.0.22:25317/D_Drive/ryan%20music//%E8%B6%85%E7%B5%B6%E2%98%86%E3%83%80%E3%82%A4%E3%83%8A%E3%83%9F%E3%83%83%E3%82%AF%EF%BC%81%E3%80%90short%20ver.%E3%80%91%20_%20%E5%90%89%E4%BA%95%E5%92%8C%E5%93%89.mp4"

s=urllib.unquote(link)
l=[s]
print l
l.append(s.decode('utf8'))
print l

address = "192.168.0.22:25317"
savedir="C:/Metafora"
page = urllib2.urlopen("http://%s"%address,timeout=10).read()
soup = BeautifulSoup(page)
links = soup.find_all('a')
for a in links:
    print a['href']
    filename = os.path.basename(urllib.unquote(a['href']))
    data = urllib2.urlopen("http://"+address+"/"+a['href']).read()
    f = open(savedir+"/"+filename.decode('utf8'),"wb")
    f.write(data)
    f.close()
