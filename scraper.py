import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
total_sum = 0;
count = 0;
for tag in tags:
	count += 1
	total_sum += int(tag.contents[0])

print 'Count',count
print total_sum