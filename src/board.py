import numpy as np

# Constants
board_width = 7
board_height = 6
EMPTY = 0
AI = 1
HUMAN = 2

# Count the number of nodes visited during the game search
COUNT = 0

def increment_count():
    global COUNT
    COUNT += 1

def reset_count():
    global COUNT
    COUNT = 0

def get_count():
    return COUNT

board_symbol_mapping_ascii = {
    EMPTY: ' ',
    HUMAN: 'X',
    AI: 'O'
}

def board_initialize(width, height):
    """Create a new ConnectFourBoard as a numpy array."""
    board = np.zeros((height, width), dtype=int)
    return board

def print_board(board):
    """Print out the current board in ASCII format."""
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {board_symbol_mapping_ascii[cell]} ", end="|")
        print()
    print("-" * (board.shape[1] * 4 + 1))
    print("  " + "   ".join(str(i) for i in range(board.shape[1])))

def get_curr_row_by_col(board, column):
    """Get the position of the lowest unoccupied cell within the specific column."""
    # Note: board_height is used globally here as per original notebook
    for row in range(board_height - 1, -1, -1):
        if board[row][column] == 0:
            return row
    return None

def is_location_valid(board, column):
    """Check if the target column is still not full."""
    return board[0][column] == 0

def drop_disc(board, column, player_id):
    """Add a disc to the target column on the board."""
    row = get_curr_row_by_col(board, column)
    if is_location_valid(board, column) and row is not None:
        board[row][column] = player_id
    else:
        raise ValueError("Invalid Move: Column is full or out of bounds")

def is_full(board):
    """Check if the board is completely full."""
    return all(cell != 0 for row in board for cell in row)
