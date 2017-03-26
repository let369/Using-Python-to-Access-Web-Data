import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

total=0

results = tree.findall('comments/comment')
print "Count: " , len(results)

for item in results:
	stnum = item.find('count').text
	num = int(stnum)
	total += num;

print "Sum: " , total;
