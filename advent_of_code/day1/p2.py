'''
Sonar sweep problem. From a list of depth measurement, count the times
when the depth is increases. 
Part 2: comparison is done for a three-measurement-window 
'''
import numpy as np

count = 0
three_sum = np.array([])

with open('data.txt','r') as fp:
	d1 = fp.readline()
	d2 = fp.readline()
	while True:
		d3 = fp.readline()
		if not d3:
			break
		three_sum = np.append(three_sum,int(d1)+int(d2)+int(d3)) 
		d1 = d2
		d2 = d3
for i in range(len(three_sum)-1):
	if (three_sum[i+1] > three_sum[i]):
		count = count + 1

print(count)
