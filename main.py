import math
import game
import negamax as ngmx


def game_ui(board):
	print('Welcome to Connect 4!')
	while True:
		print('Choose a game option:')
		print('\t1. Player vs Player\n\t2. Player vs AI\n\t3. AI vs AI\n\t4. Exit')
		try:
			game_option = int(input('Option: '))
		except KeyboardInterrupt:
			break
		except:
			print('Invalid option, try again.')
			continue
		if game_option == 1:
			player_vs_player(board)
			break
		elif game_option == 2:
			try:
				heuristic_num = int(input('Choose a heuristic (1, 2 or 3): '))
			except:
				print('Invalid option, try again.')
				continue
			player_vs_ai(board, heuristic_num)
			break
		elif game_option == 3:
			try:
				heuristic_num1 = int(input('Choose a heuristic for 1st AI (1, 2 or 3): '))
				heuristic_num2 = int(input('Choose a heuristic for 2nd AI (1, 2 or 3): '))
			except:
				print('Invalid option, try again.')
				continue
			ai_vs_ai(board, heuristic_num1, heuristic_num2)
			break
		elif game_option == 4:
			break
		else:
			print('Invalid option, try again.')


def player_vs_player(board):
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

def player_vs_ai(board, hueristic_num):
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
			column, score = ngmx.negamax(state=state, depth=0, max_depth=5, isMaximizer=True, alpha=-math.inf, beta=math.inf, heuristic_num=hueristic_num)
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

def ai_vs_ai(board, hueristic_num_1, hueristic_num_2):
	turn = 'X'
	while True:
		if turn == 'X':
			state = [row.copy() for row in board]
			column, score = ngmx.negamax(state=state, depth=0, max_depth=4, isMaximizer=True, alpha=-math.inf, beta=math.inf, heuristic_num=hueristic_num_1)
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
		else:
			state = [row.copy() for row in board]
			column, score = ngmx.negamax(state=state, depth=0, max_depth=4, isMaximizer=True, alpha=-math.inf, beta=math.inf, heuristic_num=hueristic_num_2)
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

def main():
	board = [[' ']*8 for _ in range(7)]
	game_ui(board)

if __name__ == '__main__':
	main()