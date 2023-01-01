# connect four game with a 6x7 board

import random
import sys

# board is a list of 6 lists, each containing 7 items
# the items are either ' ', 'X', or 'O'
board = [[' ']*7 for i in range(6)]

def print_board():
	print(' 1 2 3 4 5 6 7')
	for row in board:
			print('|' + '|'.join(row) + '|')
	print('---------------')

def is_valid_move(col):
	if col < 1 or col > 7:
		return False
	return board[0][col-1] == ' '

def make_move(col, ox):
	for row in range(5, -1, -1):
		if board[row][col-1] == ' ':
			break
	board[row][col-1] = ox

def is_win(ox):
	# check horizontal spaces
	for c in range(4):
		for r in range(6):
			if board[r][c] == ox and board[r][c+1] == ox and board[r][c+2] == ox and board[r][c+3] == ox:
				return True

	# check vertical spaces
	for c in range(7):
		for r in range(3):
			if board[r][c] == ox and board[r+1][c] == ox and board[r+2][c] == ox and board[r+3][c] == ox:
				return True

	# check / diagonal spaces
	for c in range(4):
		for r in range(3):
			if board[r][c] == ox and board[r+1][c+1] == ox and board[r+2][c+2] == ox and board[r+3][c+3] == ox:
				return True

	# check \ diagonal spaces
	for c in range(4):
		for r in range(3, 6):
			if board[r][c] == ox and board[r-1][c+1] == ox and board[r-2][c+2] == ox and board[r-3][c+3] == ox:
				return True

def is_draw():
	for row in board:
		for col in row:
			if col == ' ':
				return False
	return True

def computer_move():
	# first, try to win in the next move
	for c in range(1, 8):
		if is_valid_move(c):
			make_move(c, 'O')
			if is_win('O'):
				return
			# undo move
			board[5][c-1] = ' '

	# check if the player could win on his next move, and block that move
	for c in range(1, 8):
		if is_valid_move(c):
			make_move(c, 'X')
			if is_win('X'):
				make_move(c, 'O')
				return
			# undo move
			board[5][c-1] = ' '

	# try to take one of the corners, if they are free
	move = random.choice([1, 3, 5, 7])
	if is_valid_move(move):
		make_move(move, 'O')
		return

	# move in the center, if it is free
	if is_valid_move(4):
		make_move(4, 'O')
		return

	# move on one of the sides
	move = random.choice([2, 6])
	make_move(move, 'O')

def main():
	while True:
		print_board()
		# get player 1 input
		while True:
			move = input('X) Your move? ')
			if move.lower().startswith('q'):
				print('Thanks for playing!')
				sys.exit()
			if move.isdigit():
				move = int(move)
				if is_valid_move(move):
					break
				print('Column', move, 'is full!')
			else:
				print('That is not a valid column number!')

		make_move(move, 'X')
		if is_win('X'):
			print_board()
			print('X) You win!')
			break
		if is_draw():
			print_board()
			print('It is a draw!')
			break

		# get player 2 input
		computer_move()
		if is_win('O'):
			print_board()
			print('O) I win!')
			break
		if is_draw():
			print_board()
			print('It is a draw!')
			break

if __name__ == '__main__':
	main()