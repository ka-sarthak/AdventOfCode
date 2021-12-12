'''
Sonar sweep problem. From a list of depth measurement, count the times
when the depth is increases. 
'''
import numpy as np

count = 0

with open('data.txt','r') as fp:
	d1 = fp.readline()
	while True:
		d2 = fp.readline()
		if not d2:
			break
		if int(d1)<int(d2):
			count = count + 1
			print(count,int(d1),int(d2))
		d1 = d2

print(count)
