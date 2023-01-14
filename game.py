# two player connect four game with a 7x8 board

import sys
import negamax as ngmx
import math

board = [[' ']*8 for i in range(7)]

def print_board():
	print(' 1 2 3 4 5 6 7 8')
	for row in board:
			print('|' + '|'.join(row) + '|')
	print('-----------------')

def is_valid_move(col):
	if col < 1 or col > 8:
		return False
	return board[0][col-1] == ' '

def is_next_move_valid(state, col):
    if col < 1 or col > 8:
        return False
    return state[0][col-1] == ' '

def get_possible_moves(state):
    moves = []
    for col in range(1,9):
        if is_next_move_valid(state, col):
            moves.append(col)
    return moves

def make_move_with_state(state, column, letter):
	for row in range(6, -1, -1):
		if state[row][column-1] == ' ':
			state[row][column-1] = letter
			break

def make_move(col, letter):
	for row in range(6, -1, -1):
		if board[row][col-1] == ' ':
			board[row][col-1] = letter
			break

def is_winner(letter):
	# check horizontal spaces
	for row in board:
		for col in range(4):
			if row[col] == letter and row[col+1] == letter and row[col+2] == letter and row[col+3] == letter:
				return True
	# check vertical spaces
	for col in range(8):
		for row in range(3):
			if board[row][col] == letter and board[row+1][col] == letter and board[row+2][col] == letter and board[row+3][col] == letter:
				return True
	# check / diagonal spaces
	for row in range(3):
		for col in range(4):
			if board[row][col] == letter and board[row+1][col+1] == letter and board[row+2][col+2] == letter and board[row+3][col+3] == letter:
				return True
	# check \ diagonal spaces
	for row in range(3, 6):
		for col in range(4):
			if board[row][col] == letter and board[row-1][col+1] == letter and board[row-2][col+2] == letter and board[row-3][col+3] == letter:
				return True

def is_board_full():
	for row in board:
		for col in row:
			if col == ' ':
				return False
	return True

def main():
	print_board()
	turn = 'X'
	while True:
		if turn == 'X':
			try:
				col = int(input('Player %s, choose your column (1-8): ' % turn))
			except:
				print('Invalid move, try again.')
				continue
			if is_valid_move(col):
				make_move(col, turn)
				if is_winner(turn):
					print_board()
					print('Player wins!' % turn)
					sys.exit()
				turn = 'O' if turn == 'X' else 'X'
				print_board()
			else:
				print('Invalid move, try again.')
			if is_board_full():
				print('The game is a tie!')
				sys.exit()
		else:
			column, score = ngmx.negamax(state=board, depth=0, max_depth=5, isMaximizer=True, alpha=-math.inf, beta=math.inf)
			if is_valid_move(board, column):
				make_move(column, turn)

				if is_winner(turn):
					print_board()
					print('AI wins!' % turn)
					sys.exit()

				turn = 'O' if turn == 'X' else 'X'
				print_board()
    
				if is_board_full():
					print('The game is a tie!')
					sys.exit()


if __name__ == '__main__':
	main()