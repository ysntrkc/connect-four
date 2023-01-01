# two player connect four game with a 6x7 board

import sys

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

def make_move(col, letter):
	for row in range(5, -1, -1):
		if board[row][col-1] == ' ':
			board[row][col-1] = letter
			break

def is_winner(letter):
	# check horizontal spaces
	for c in range(4):
		for r in range(6):
			if board[r][c] == letter and board[r][c+1] == letter and board[r][c+2] == letter and board[r][c+3] == letter:
				return True
	# check vertical spaces
	for c in range(7):
		for r in range(3):
			if board[r][c] == letter and board[r+1][c] == letter and board[r+2][c] == letter and board[r+3][c] == letter:
				return True
	# check / diagonal spaces
	for c in range(4):
		for r in range(3):
			if board[r][c] == letter and board[r+1][c+1] == letter and board[r+2][c+2] == letter and board[r+3][c+3] == letter:
				return True
	# check \ diagonal spaces
	for c in range(4):
		for r in range(3, 6):
			if board[r][c] == letter and board[r-1][c+1] == letter and board[r-2][c+2] == letter and board[r-3][c+3] == letter:
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
			col = int(input('Player %s, choose your column (1-7): ' % turn))
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