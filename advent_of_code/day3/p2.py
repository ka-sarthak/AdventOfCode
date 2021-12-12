'''
Decoding binary numbers to get two different (more trickier than before)
quantities in binary
'''

import numpy as np

with open('data.txt', 'r') as fp:
	raw = np.array(list(fp.readline())[:-1]).astype(int)
	while True:
		dp = np.array(list(fp.readline())[:-1]).astype(int)
		if dp.size == 0:
			break
		raw = np.vstack((raw,dp))	# stacks each line (which has array of bits) 
						# vertically
# filtering for o2
filtered = raw
for i in range(raw.shape[1]):
	if len(filtered.shape)==1:
		break
	most_freq = (np.sum(filtered[:,i])/len(filtered) >= 0.5) * 1
	filtered = filtered[np.where(filtered[:,i] == most_freq),:].squeeze()
o2 = filtered

# filtering for co2
filtered = raw
for i in range(raw.shape[1]):
	if len(filtered.shape)==1:
		break
	least_freq = (np.sum(filtered[:,i])/len(filtered) < 0.5) * 1
	filtered = filtered[np.where(filtered[:,i] == least_freq),:].squeeze()
co2 = filtered

print(o2,co2)

o2str = str()
co2str = str()
for i in o2:
	o2str = o2str + f'{i}'
for i in co2:
	co2str = co2str + f'{i}'

print('Life support remaining =', int(o2str,2) * int(co2str,2))
