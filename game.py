def print_board(board):
	print(' 1 2 3 4 5 6 7 8')
	for row in board:
			print('|' + '|'.join(row) + '|')
	print('-----------------')

def is_valid_move(board, col):
	if col < 1 or col > 8:
		return False
	return board[0][col-1] == ' '

def get_possible_moves(board):
    moves = []
    for col in range(1,9):
        if is_valid_move(board, col):
            moves.append(col)
    return moves

def make_move(board, col, letter):
	for row in range(6, -1, -1):
		if board[row][col-1] == ' ':
			board[row][col-1] = letter
			break
	return board

def is_winner(board, letter):
	# check horizontal spaces
	for row in board:
		for col in range(4):
			if row[col] == letter and row[col+1] == letter and row[col+2] == letter and row[col+3] == letter:
				return True
	# check vertical spaces
	for col in range(8):
		for row in range(4):
			if board[row][col] == letter and board[row+1][col] == letter and board[row+2][col] == letter and board[row+3][col] == letter:
				return True
	# check / diagonal spaces
	for col in range(5):
		for row in range(4):
			if board[row][col] == letter and board[row+1][col+1] == letter and board[row+2][col+2] == letter and board[row+3][col+3] == letter:
				return True
	# check \ diagonal spaces
	for col in range(5):
		for row in range(3, 7):
			if board[row][col] == letter and board[row-1][col+1] == letter and board[row-2][col+2] == letter and board[row-3][col+3] == letter:
				return True

def is_board_full(board):
	for row in board:
		for col in row:
			if col == ' ':
				return False
	return True
