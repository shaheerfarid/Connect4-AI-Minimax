import math
from .board import is_location_valid, drop_disc, HUMAN, AI, increment_count
from .rules import winning_move, is_terminal_node
from .evaluation import evaluate_position

def get_valid_columns(board):
    """Return the non-full columns in the current board."""
    return [c for c in range(board.shape[1]) if is_location_valid(board, c)]

def minimax(board, depth, do_max, player):
    """Make an AI decision using the Minimax algorithm."""
    increment_count()
    
    opponent = HUMAN if player == AI else AI
    valid_columns = get_valid_columns(board)
    is_terminal = is_terminal_node(board)
    
    if depth == 0 or is_terminal:
        return None, evaluate_position(board, player)
    
    if do_max:
        value = -math.inf
        column = valid_columns[0]
        for col in valid_columns:
            b_copy = board.copy()
            drop_disc(b_copy, col, player)
            new_score = minimax(b_copy, depth-1, False, player)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else:
        value = math.inf
        column = valid_columns[0]
        for col in valid_columns:
            b_copy = board.copy()
            drop_disc(b_copy, col, opponent)
            new_score = minimax(b_copy, depth-1, True, player)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value

def alpha_beta_pruning(board, depth, alpha, beta, do_max, player):
    """Make an AI decision using Minimax with Alpha-Beta Pruning."""
    increment_count()
    
    opponent = HUMAN if player == AI else AI
    valid_columns = get_valid_columns(board)
    is_terminal = is_terminal_node(board)
    
    if depth == 0 or is_terminal:
        return None, evaluate_position(board, player)
    
    if do_max:
        value = -math.inf
        column = valid_columns[0]
        for col in valid_columns:
            b_copy = board.copy()
            drop_disc(b_copy, col, player)
            new_score = alpha_beta_pruning(b_copy, depth-1, alpha, beta, False, player)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = valid_columns[0]
        for col in valid_columns:
            b_copy = board.copy()
            drop_disc(b_copy, col, opponent)
            new_score = alpha_beta_pruning(b_copy, depth-1, alpha, beta, True, player)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
