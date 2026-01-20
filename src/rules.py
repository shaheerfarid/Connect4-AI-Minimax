from .board import HUMAN, AI

def winning_move(board, player_id):
    """Check if player_id has won on the current board state."""
    # Check horizontal locations for win
    for c in range(board.shape[1]-3):
        for r in range(board.shape[0]):
            if board[r][c] == player_id and board[r][c+1] == player_id and board[r][c+2] == player_id and board[r][c+3] == player_id:
                return True

    # Check vertical locations for win
    for c in range(board.shape[1]):
        for r in range(board.shape[0]-3):
            if board[r][c] == player_id and board[r+1][c] == player_id and board[r+2][c] == player_id and board[r+3][c] == player_id:
                return True

    # Check positively sloped diagonals
    for c in range(board.shape[1]-3):
        for r in range(board.shape[0]-3):
            if board[r][c] == player_id and board[r+1][c+1] == player_id and board[r+2][c+2] == player_id and board[r+3][c+3] == player_id:
                return True

    # Check negatively sloped diagonals
    for c in range(board.shape[1]-3):
        for r in range(3, board.shape[0]):
            if board[r][c] == player_id and board[r-1][c+1] == player_id and board[r-2][c+2] == player_id and board[r-3][c+3] == player_id:
                return True
    return False

def is_terminal_node(board):
    """Check if the game has ended (someone won or board is full)."""
    from .minimax import get_valid_columns
    return winning_move(board, HUMAN) or winning_move(board, AI) or len(get_valid_columns(board)) == 0