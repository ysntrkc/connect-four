import math
import game

# Utility score calculator for heuristic 1
def calculate_sequence_heuristic_1(sequence, coin, isDiagonal):
    if coin == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    utility = 0

    # using count function we count the number of items in that sequence.
    # In this section we give points for our own sequences.
    # Diagonal sequnce gives extra points.
    if sequence.count(coin) == 4:
        utility += 4 + isDiagonal

    elif sequence.count(coin) == 3 and sequence.count(' ') == 1:
        utility += 3 + isDiagonal

    elif sequence.count(coin) == 2 and sequence.count(' ') == 2:
        utility += 2 + isDiagonal

    elif sequence.count(coin) == 1 and sequence.count(' ') == 3:
        utility += 1 + isDiagonal

    # In this part we check the opponent pieces and get utility scores for blocking.
    if sequence.count(opponent) == 3 and sequence.count(' ') == 1:
        utility -= 27

    elif sequence.count(opponent) == 2 and sequence.count(' ') == 2:
        utility -= 4

    elif sequence.count(opponent) == 1 and sequence.count(' ') == 3:
        utility -= 1

    return utility

# Utility score calculator for heuristic 2
def calculate_sequence_heuristic_2(sequence, coin, isDiagonal, col):
    if coin == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    # With this calculation we priorizite middle section.
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

# Utility score calculator for heuristic 3 
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

    #Checks for diagonal score on the board.
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

# Minimax function with alpha - beta pruning.
def negamax(state, depth, max_depth, isMaximizer, alpha, beta, heuristic_num):
    # Since this is a recursive function we only return values when game is over or we reach maximum depth of our search.
    if depth == max_depth or game.is_winner(state, 'X') or game.is_winner(state, 'O') or game.is_board_full(state):
        if game.is_winner(state, 'X'):
            return [-1, math.inf]   # If X is winner give max value.
        elif game.is_winner(state, 'O'):
            return [-1, -math.inf]  # If O is winner give min value
        elif game.is_board_full(state):
            return [-1, 0]      # If draw give 0
        else:   
            return [-1, utility_score(state, isMaximizer, heuristic_num)]   # Else return the utility value and column position using utility_score function.

    # Operations for maximizer node.
    # We update alpha according to score.
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

    # Operations for minimizer node.
    # We update beta according to score.
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
