import math
import game
import negamax as ngmx


def main():
	board = [[' ']*8 for i in range(7)]

	game.print_board(board)
	turn = 'X'
	while True:
		if turn == 'X':
			try:
				col = int(input(f'Player {turn}, choose your column (1-8): '))
			except KeyboardInterrupt:
				break
			except:
				print('Invalid move, try again.')
				continue
			if game.is_valid_move(board, col):
				board = game.make_move(board, col, turn)
				if game.is_winner(board, turn):
					game.print_board(board)
					print(f'Player {turn} wins!')
					break
				turn = 'O' if turn == 'X' else 'X'
				game.print_board(board)
			else:
				print('Invalid move, try again.')
			if game.is_board_full(board):
				print('The game is a tie!')
				break
		else:
			state = [row.copy() for row in board]
			column, score = ngmx.negamax(state=state, depth=0, max_depth=5, isMaximizer=True, alpha=-math.inf, beta=math.inf)
			if game.is_valid_move(board, column):
				board = game.make_move(board, column, turn)

				if game.is_winner(board, turn):
					game.print_board(board)
					print(f'AI {turn} wins!')
					break

				turn = 'O' if turn == 'X' else 'X'
				game.print_board(board)

				if game.is_board_full(board):
					print('The game is a tie!')
					break

if __name__ == '__main__':
	main()