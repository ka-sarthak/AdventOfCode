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
			line = fp.readline()[:-1]     # keep an empty last line in data
			if not line:
				break
			line = line.split(' -> ')
			aux[0] = int(line[0].split(',')[0])
			aux[1] = int(line[0].split(',')[1])
			aux[2] = int(line[1].split(',')[0])
			aux[3] = int(line[1].split(',')[1])
			ep = np.append(ep,aux)
	ep = ep.reshape((-1,4))
	return ep.astype(int)

def classifyLines(ep):
	'''
	separates the lines into vertical, horizontal and general lines
	'''
	vep = np.array([])
	hep = np.array([])
	dep = np.array([])
	for i in ep:
		if i[0] == i[2]:
			vep = np.append(vep, i)
		elif i[1] == i[3]:
			hep = np.append(hep, i)
		else:
			dep = np.append(dep, i)
	
	vep = vep.reshape((-1,4)).astype(int)
	hep = hep.reshape((-1,4)).astype(int)
	dep = dep.reshape((-1,4)).astype(int)

	return vep, hep, dep

def plotLines(lines, type):
	plotted = np.array([])
	
	# type 1: vertical
	if type == 1:
		for i in lines.reshape((-1,4)):
			inc = np.sign(i[3]-i[1])
			inter = i[1]
			while True:
				plotted = np.append(plotted, [i[0],inter])
				if inter == i[3]:
					break
				inter = inter + inc*1

	# type 2: horizontal
	if type == 2:
		for i in lines.reshape((-1,4)):
			inc = np.sign(i[2]-i[0])
			inter = i[0]
			while True:
				plotted = np.append(plotted, [inter, i[1]])
				if inter == i[2]:
					break
				inter = inter + inc*1
	
	plotted = plotted.reshape((-1,2))
	return plotted.astype(int)

def plotSpace(lines):
	
	xmax = np.max(lines[:,0])
	xmin = np.min(lines[:,0])
	ymax = np.max(lines[:,1])
	ymin = np.min(lines[:,1])
	print(f'[ymax,xmax]=[{ymax},{xmax}]')
	print(f'[ymin,xmin]=[{ymin},{xmin}]')
	space = np.zeros((ymax-ymin+1, xmax-xmin+1))
	
	for pt in lines:
		x = pt[0] - xmin
		y = pt[1] - ymin
		space[y,x] = space[y,x] + 1

	return space.astype(int)

#######################################

ep = getEndPoints(filename)
vep, hep, dep = classifyLines(ep)

plot1 = plotLines(vep,1)
plot2 = plotLines(hep,2)
plot = np.vstack((plot1, plot2))

space = plotSpace(plot)

sum = 0 
for i in space.flatten():
	if i > 1:
		sum=sum+1
print(f'Total points where more than 1 horizontal or vertical lines cross: {sum}')
