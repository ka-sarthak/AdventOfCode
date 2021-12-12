'''
Decoding binary numbers to get two different quantities in binary
'''

import numpy as np

raw = np.array([])
with open('data.txt', 'r') as fp:
	raw = np.array(list(fp.readline())[:-1]).astype(int)
	while True:
		dp = np.array(list(fp.readline())[:-1]).astype(int)
		if dp.size == 0:
			break
		raw = np.vstack((raw,dp))	# stacks each line (which has array of bits) 
						# vertically

decoded = np.sum(raw, axis=0)/len(raw)		# if sum/n > 0.5, more ones than zeros
gamma_rate = (decoded > 0.5)*1			
epsilon_rate = (decoded < 0.5)*1

gstr = str()
estr = str()
for i in gamma_rate:
	gstr = gstr + f'{i}'
for i in epsilon_rate:
	estr = estr + f'{i}'

print('Power consumption =', int(gstr,2) * int(estr,2))
