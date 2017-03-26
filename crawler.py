import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
cou = raw_input('Enter count: ')
pos = raw_input('Enter position: ')
count = int(cou)
position = int(pos)

name_list = list()
i=0

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

print 'Retrieving:',url
while(i<count):
	counter = 0
	for tag in tags:
		counter += 1
		if(counter==position):
			print 'Retrieving:',tag.get('href', None)
			html = urllib.urlopen(tag.get('href', None)).read()
			soup = BeautifulSoup(html)
			tags = soup('a')
			i=i+1