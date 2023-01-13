from game import *
import math

def utility_score(state, turn):
    print()
    

def negamax(state, depth, max_depth, isMaximizer, alpha, beta):
    if depth == max_depth or is_winner('X') or is_winner('O') or is_board_full(): 
        
        if is_winner('X'):
            return [-1, math.inf]
        elif is_winner('O'):
            return [-1, -math.inf]
        elif is_board_full():
            return [-1, 0]
        else:
            return [-1, utility_score(state, isMaximizer)]

    if isMaximizer == True:
        value = -math.inf
        moves = get_possible_moves(state)
        best_column = moves[0]
        for column in moves:
            copied_state = state.copy()
            make_move_with_state(copied_state, column, 'X')
            score = negamax(copied_state, depth+1, False)[1]
            if score > value:
                value = score
                best_column = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_column, value
                
    else:
        value = math.inf
        moves = get_possible_moves(state)
        best_column = moves[0]
        for column in moves:
            copied_state = state.copy()
            make_move_with_state(copied_state, column, 'O')
            score = negamax(copied_state, depth+1, True)[0]
            if score < value:
                value = score
                best_column = column
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_column, value

    