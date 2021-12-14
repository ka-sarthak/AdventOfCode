''' Game of Bingo with the Squid'''
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

def win_sweep(board_arr):
    '''
    sweeps for 5 consecutive markings on both rows
    '''
    winner = 0
    win_ind = len(board_arr[0]+1)
    for i in np.arange(0,len(board_arr[0]),5):
        if np.all(board_arr[0,i:i+5] == -1):
            winner = 1
            win_ind = int(i/25)
            break

    if winner == 0:
        for i in np.arange(0,len(board_arr[1]),5):
            if np.all(board_arr[1,i:i+5] == -1):
                winner = 1
                win_ind = int(i/25)
                break
    
    if winner == 1:
        win_ind = int(i/25)
    
    return win_ind

##########################################

nums = getNumbers(filename)
boards = getBoards(filename)

for i in nums:
    boards = mark_sweep(boards,i)
    win_ind = win_sweep(boards)
    if win_ind < len(boards[0]):
        break

win_board = boards[0,win_ind*25:win_ind*25+25]

## Winner board and Score calculation
win_board = boards[0,win_ind*25:win_ind*25+25]
score = i * np.sum(np.array([0 if i == -1 else i for i in win_board]))

print(f"The board that wins is #{win_ind} with a score of {score}.")
print(win_board.reshape((5,5)))

