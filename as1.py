import re
hand = open ('as1.txt')
n = list()
total_sum = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for x in range(0,len(stuff)):
    	n.append(stuff[x])
for x in n:
	total_sum = total_sum + int(x)
print total_sum