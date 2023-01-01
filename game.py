# two player connect four game with a 7x8 board

import sys

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
		try:
			col = int(input('Player %s, choose your column (1-8): ' % turn))
		except:
			print('Invalid move, try again.')
			continue
		if is_valid_move(col):
			make_move(col, turn)
			if is_winner(turn):
				print_board()
				print('Player %s wins!' % turn)
				sys.exit()
			turn = 'O' if turn == 'X' else 'X'
			print_board()
		else:
			print('Invalid move, try again.')
		if is_board_full():
			print('The game is a tie!')
			sys.exit()

if __name__ == '__main__':
	main()