''' Game of Bingo with the Squid (Reverse)
    Which board wins the last?
'''
import numpy as np
filename = 'data.txt'

def getNumbers(filename):
    '''
    returns an array of the numbers to be drawn 
    '''
    with open(filename, 'r') as fp:
        num_arr = np.array(fp.readline()[:-1].split(',')).astype(int)
    
    return num_arr

def getBoards(filename):
    '''
    returns a 2-D array corresponding to a row of all board entries
    swept row-wise from the data and a row of all board entries swept 
    col-wise from the data. 
    '''
    board_arr = np.array([])
    with open(filename, 'r') as fp:
        _ = fp.readline()          # skip first line

        row1 = np.array([])
        row2 = np.array([])
        
        while True:
            line = fp.readline()
        
            if not line:
                break
            
            board = np.array([])
            for i in range(5):
                board = np.append(board, np.array(fp.readline()[:-1].split()).astype(int))
            row1 = np.append(row1, board)
            row2 = np.append(row2, board.reshape((5,5)).T.flatten())

    board_arr = np.vstack((row1, row2))
    
    with open(filename, 'r') as fp:
        for lastline in fp:
            pass
    last = lastline.split()[-1]
    board_arr[:,-1] = int(last)
    
    return board_arr

def mark_sweep(board_arr, num):
    '''
    marks the boards if num is encountered
    '''
    marked_arr = np.array([[-1 if x==num else x for x in row] for row in board_arr])
    
    return marked_arr

def win_sweep(board_arr, win_list):
    '''
    sweeps for 5 consecutive markings on both rows
    '''
    winner = 0
    for i in range(int(len(board_arr[0])/25)):
        if i in win_list:
            continue
        for j in np.arange(i*25,(i+1)*25,5):
            if np.all(board_arr[0,j:j+5] == -1):
                win_list = np.append(win_list, i)
                winner = 1 
                break

    for i in range(int(len(board_arr[1])/25)):
        if i in win_list:
            continue
        for j in np.arange(i*25,(i+1)*25,5):
            if np.all(board_arr[1,j:j+5] == -1):
                win_list = np.append(win_list, i)
                winner = 1 
                break

    return winner, win_list

##########################################

nums = getNumbers(filename)
boards = getBoards(filename)
clean = boards

win_list = np.array([])
for i in nums:
    boards = mark_sweep(boards,i)
    winner, win_list = win_sweep(boards,win_list)
    if len(win_list) == 100:
        break
    if len(win_list)==1 and winner==1:          # for getting the first board completed
        saved_state = boards
        saved_i = i

''' Solution for problem 1: 
    First one is the winner '''
#i = int(saved_i)
#win_idx = int(win_list[0])
#win_board = saved_state[0,win_idx*25:win_idx*25+25]

''' Solution for problem 2:
    Last one is the winner  '''
win_idx = int(win_list[-1])
win_board = boards[0,win_idx*25:win_idx*25+25]

## Score calculation
score = i * np.sum(np.array([0 if i == -1 else i for i in win_board]))

print(f"The board that wins is #{win_idx} with a score of {score}.")
print(f'Original Board #{win_idx}:\n', clean[0,win_idx*25:win_idx*25+25].reshape((5,5)))
print(f'Marked Board #{win_idx} after drawing the last number {i}:\n', win_board.reshape((5,5)))
