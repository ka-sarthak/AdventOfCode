'''
	Hydrothermal vents 
	Given end points of line segments, find the grid points through 
	which >=2 lines pass. 
'''
import numpy as np
import re

filename = 'data.txt'

def getEndPoints(filename):
	'''
	gets the ends points from input file
	'''
	ep = np.array([])
	aux = np.zeros(4)
	with open(filename, 'r') as fp:
		while True:
			line = fp.readline()[:-1]
			if not line:
				break
			line = line.split(' -> ')
			aux[0] = int(line[0].split(',')[0])
			aux[1] = int(line[0].split(',')[1])
			aux[2] = int(line[1].split(',')[0])
			aux[3] = int(line[1].split(',')[1])
			ep = np.append(ep,aux)
	
	return ep.reshape((-1,4)).astype(int)

def Lines(ep):
	'''
	separates the lines into vertical, horizontal and general lines
	'''
	vep = np.array([])
	hep = np.array([])
	gep = np.array([])
	for i in ep:
		if i[0] == i[2]:
			vep = np.append(vep, i)
		elif i[1] == i[3]:
			hep = np.append(hep, i)
		else:
			gep = np.append(gep, i)
	
	vep = vep.reshape((-1,4)).astype(int)
	hep = hep.reshape((-1,4)).astype(int)
	gep = gep.reshape((-1,4)).astype(int)

	return vep, hep, gep

def plotLines(lines, type):
	plotted = np.array([])
	
	# type 1: vertical
	if type == 1:
		for i in lines.reshape((-1,4)):
			for j in range(i[1],i[3]+1):
				plotted = np.append(plotted, [i[0],j])

	# type 2: horizontal
	if type == 2:
		for i in lines.reshape((-1,4)):
			for j in range(i[0],i[2]+1):
				plotted = np.append(plotted, [j, i[1]])

	return plotted.reshape((-1,2)).astype(int)
def plotSpace(lines):
	#xmax = np.max(lines[0])
	#xmin = np.min(lines[0])
	#ymax = np.max(lines[1])
	#ymin = np.min(lines[1])
	#space = np.zeros((xmax-xmin+1, ymax-ymin+1))
	#lines = lines - [xmin,ymin]
	space = np.zeros((1000,1000))
	for pt in lines:
		space[pt[0]-1,pt[1]-1] = space[pt[0]-1,pt[1]-1] + 1

	return space
def countOccur(plot):
	'''
	counts the number of lines that passes through the same point
	returns list of points with their number of occurences
	'''
	numOccur = np.array([])
	i = 0
	while True:
		if i==len(plot):
			break
		curr = plot.reshape((-1,2))[i]
		idx = np.array([])
		count = 1
		for j in range(i+1,len(plot)):
			next = plot.reshape((-1,2))[j]
			if not np.all(next):
				break
			if np.all(curr == next):
				idx = np.append(idx,j)
				count = count + 1
				break
		plot = np.delete(plot, idx.astype(int), axis=0)
		numOccur = np.append(numOccur,count)	
		i = i+1
	res = np.hstack((plot.reshape((-1,2)), np.expand_dims(numOccur, axis=1)))

	return res.astype(int)
		
#######################################

ep = getEndPoints(filename)
vep, hep, gep = Lines(ep)

plot1 = plotLines(vep,1)
plot2 = plotLines(hep,2)
plot = np.vstack((plot1, plot2))
space = plotSpace(plot)
sum = 0 
for i in space.flatten():
	if i >=2:
		sum=sum+1
print(sum)
print(plot.shape)
'''
plot1 = plotLines(vep,1)
plot2 = plotLines(hep,2)
plot = np.vstack((plot1, plot2))
print(plot1[1:10], plot2[1:10], plot.shape)
#j,num = np.unique(plot, return_counts = True)
print(j.shape)
print(num)
#print(countOccur(plot).shape)
'''
