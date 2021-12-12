'''
Navigation of the submarine. To compute the final position using initial state = (0,0,0)
and input data of up, down, forward. Here the state represent (horizontal, depth, aim)
with some complicated relation between commands and states - look on the website.
'''
import numpy as np

initial_pos = np.array([0,0,0])
with open('data.txt', 'r') as fp:
	while True:
		command = fp.readline().split()
		if not command:
			break
		if command[0] == 'forward':
			initial_pos[0] = initial_pos[0] + int(command[1])
			initial_pos[1] = initial_pos[1] + int(command[1])*initial_pos[2]
		elif command[0] == 'up':
			initial_pos[2] = initial_pos[2] - int(command[1])
		elif command[0] == 'down':
			initial_pos[2] = initial_pos[2] + int(command[1]) 
		else:
			print(f"Invalid command! Can't process {command[0]}")
print(f'Final position = {initial_pos}') 
print('Product = ', initial_pos[0]*initial_pos[1])
