import math
import game

def calculate_sequence_heuristic_1(sequence, coin, isDiagonal):
    if coin == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    utility = 0

    if sequence.count(coin) == 4:
        utility += 4 + isDiagonal

    elif sequence.count(coin) == 3 and sequence.count(' ') == 1:
        utility += 3 + isDiagonal

    elif sequence.count(coin) == 2 and sequence.count(' ') == 2:
        utility += 2 + isDiagonal

    elif sequence.count(coin) == 1 and sequence.count(' ') == 3:
        utility += 1 + isDiagonal

    if sequence.count(opponent) == 3 and sequence.count(' ') == 1:
        utility -= 27

    elif sequence.count(opponent) == 2 and sequence.count(' ') == 2:
        utility -= 4

    elif sequence.count(opponent) == 1 and sequence.count(' ') == 3:
        utility -= 1

    return utility

def calculate_sequence_heuristic_2(sequence, coin, isDiagonal, col):
    if coin == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    utility = 2 - ((((col - 3.5) ** 2)) / 6.125)

    if sequence.count(coin) == 4:
        utility += 4 + isDiagonal

    elif sequence.count(coin) == 3 and sequence.count(' ') == 1:
        utility += 3 + isDiagonal

    elif sequence.count(coin) == 2 and sequence.count(' ') == 2:
        utility += 2 + isDiagonal

    elif sequence.count(coin) == 1 and sequence.count(' ') == 3:
        utility += 1 + isDiagonal

    if sequence.count(opponent) == 3 and sequence.count(' ') == 1:
        utility -= 15

    elif sequence.count(opponent) == 2 and sequence.count(' ') == 2:
        utility -= 4

    elif sequence.count(opponent) == 1 and sequence.count(' ') == 3:
        utility -= 1

    return utility

def calculate_sequence_heuristic_3(sequence, coin, isDiagonal, col):
    if coin == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    utility = 5 - ((((col - 3.5) ** 2)) / 2.45)

    if sequence.count(coin) == 4:
        utility += 7 + isDiagonal * 2

    elif sequence.count(coin) == 3 and sequence.count(' ') == 1:
        utility += 5 + isDiagonal * 2

    elif sequence.count(coin) == 2 and sequence.count(' ') == 2:
        utility += 3 + isDiagonal * 2

    elif sequence.count(coin) == 1 and sequence.count(' ') == 3:
        utility += 1 + isDiagonal * 2

    if sequence.count(opponent) == 3 and sequence.count(' ') == 1:
        utility -= 30

    elif sequence.count(opponent) == 2 and sequence.count(' ') == 2:
        utility -= 7

    elif sequence.count(opponent) == 1 and sequence.count(' ') == 3:
        utility -= 1

    return utility

def utility_score(state, isMaximizer, heuristic_num):
    if isMaximizer:
        coin = 'X'
    else:
        coin = 'O'

    utility = 0

    # Check for vertical score.
    for c in range(8):
        column_array = [state[r][c] for r in range(7)]
        for r in range(4):
            sequence = column_array[r:r+4]
            if heuristic_num == 1:
                utility += calculate_sequence_heuristic_1(sequence, coin, 0)
            elif heuristic_num == 2:
                utility += calculate_sequence_heuristic_2(sequence, coin, 0, c)
            elif heuristic_num == 3:
                utility += calculate_sequence_heuristic_3(sequence, coin, 0, c)

    # Check for horizontal score.
    for r in range(7):
        row_array = [state[r][c] for c in range(8)]
        for c in range(5):
            sequence = row_array[c:c+4]
            if heuristic_num == 1:
                utility += calculate_sequence_heuristic_1(sequence, coin, 0)
            elif heuristic_num == 2:
                utility += calculate_sequence_heuristic_2(sequence, coin, 0, c)
            elif heuristic_num == 3:
                utility += calculate_sequence_heuristic_3(sequence, coin, 0, c)

    for r in range(4):
        for c in range(5):
            sequence = [state[r+i][c+i] for i in range(4)]
            if heuristic_num == 1:
                utility += calculate_sequence_heuristic_1(sequence, coin, 1)
            elif heuristic_num == 2:
                utility += calculate_sequence_heuristic_2(sequence, coin, 1, c)
            elif heuristic_num == 3:
                utility += calculate_sequence_heuristic_3(sequence, coin, 0, c)

    for r in range(4):
        for c in range(5):
            sequence = [state[r+3-i][c+i] for i in range(4)]
            if heuristic_num == 1:
                utility += calculate_sequence_heuristic_1(sequence, coin, 1)
            elif heuristic_num == 2:
                utility += calculate_sequence_heuristic_2(sequence, coin, 1, c)
            elif heuristic_num == 3:
                utility += calculate_sequence_heuristic_3(sequence, coin, 0, c)

    return utility


def negamax(state, depth, max_depth, isMaximizer, alpha, beta, heuristic_num):
    if depth == max_depth or game.is_winner(state, 'X') or game.is_winner(state, 'O') or game.is_board_full(state):
        if game.is_winner(state, 'X'):
            return [-1, math.inf]
        elif game.is_winner(state, 'O'):
            return [-1, -math.inf]
        elif game.is_board_full(state):
            return [-1, 0]
        else:
            return [-1, utility_score(state, isMaximizer, heuristic_num)]

    if isMaximizer == True:
        value = -math.inf
        moves = game.get_possible_moves(state)
        best_column = moves[0]
        for column in moves:
            copied_state = [row.copy() for row in state]
            game.make_move(copied_state, column, 'X')
            score = negamax(copied_state, depth+1, max_depth, False, alpha, beta, heuristic_num)[1]
            if score > value:
                value = score
                best_column = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_column, value

    else:
        value = math.inf
        moves = game.get_possible_moves(state)
        best_column = moves[0]
        for column in moves:
            copied_state = [row.copy() for row in state]
            game.make_move(copied_state, column, 'O')
            score = negamax(copied_state, depth+1,max_depth, True, alpha, beta, heuristic_num)[0]
            if score < value:
                value = score
                best_column = column
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_column, value
