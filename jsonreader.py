import urllib
import json

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
data2 = info['comments']
print 'Comments count:', len(data2)

total=0

for item in data2:
  total += item['count']
print "Total count: ", total