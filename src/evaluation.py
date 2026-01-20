from .board import HUMAN, AI

def evaluate_position(board, player):
    """An evaluation function that assigns a score to the board state."""
    score = 0
    opponent = HUMAN if player == AI else AI
    
    # Horizontal Evaluation
    for col in range(board.shape[1] - 3):
        for row in range(board.shape[0]):
            window = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            score += evaluate_window(window, player, opponent)
        
    # Vertical Evaluation
    for col in range(board.shape[1]):
        for row in range(board.shape[0] - 3):
            window = [board[row][col], board[row + 1][col], board[row + 2][col], board[row + 3][col]]
            score += evaluate_window(window, player, opponent)
    
    # Positive Slope Diagonal
    for col in range(board.shape[1] - 3):
        for row in range(board.shape[0] - 3):
            window = [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2], board[row + 3][col + 3]]
            score += evaluate_window(window, player, opponent)
    
    # Negative Slope Diagonal
    for col in range(board.shape[1] - 3):
        for row in range(3, board.shape[0]):
            window = [board[row][col], board[row - 1][col + 1], board[row - 2][col + 2], board[row - 3][col + 3]]
            score += evaluate_window(window, player, opponent)
              
    return score

def evaluate_window(window, player, opponent):
    """Utility function to score a four-cell window."""
    score = 0
    count_player = window.count(player)
    count_opponent = window.count(opponent)
    count_empty = window.count(0)

    if count_player > 0 and count_opponent == 0:
        if count_player == 4:
            score += 1000000
        elif count_player == 3:
            score += 100
        elif count_player == 2:
            score += 10
        else:
            score += 1
    elif count_opponent > 0 and count_player == 0:
        if count_opponent == 4:
            score -= 1000000
        elif count_opponent == 3:
            score -= 100
        elif count_opponent == 2:
            score -= 10
        else:
            score -= 1
            
    return score
