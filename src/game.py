import math
from .board import (
    board_initialize, print_board, drop_disc, is_location_valid, is_full,
    HUMAN, AI, board_symbol_mapping_ascii, reset_count, get_count
)
from .rules import winning_move
from .minimax import minimax, alpha_beta_pruning

def game_check(test_human, first_player, do_pruning):
    """Run a simulated game between AI and human moves."""
    winner = 0
    board = board_initialize(7, 6)
    print("{} goes first.".format(board_symbol_mapping_ascii[first_player]))
    human_count = 0
    reset_count()
    
    while True:
        if human_count >= len(test_human):
            print("No more human moves left.")
            break
            
        if first_player == AI:
            print("AI's turn")
            if do_pruning:
                col, _ = alpha_beta_pruning(board, 4, -math.inf, math.inf, True, first_player)
            else:
                col, _ = minimax(board, 4, True, first_player)
            
            drop_disc(board, col, first_player)
            print_board(board)
            
            if winning_move(board, first_player):
                print("AI wins!")
                winner = AI
                break
            first_player = HUMAN
            
        else:
            print("Human's turn.")
            col = test_human[human_count]
            human_count += 1
            if is_location_valid(board, col):
                drop_disc(board, col, first_player)
                print_board(board)
            else:
                print("Invalid move. Try next move.")
                continue
                
            if winning_move(board, first_player):
                print("You win!")
                winner = HUMAN
                break
            first_player = AI
            
        if is_full(board):
            print("It's a tie!")
            break
            
    print("Total nodes accessed by {}: {}".format(
        "Alpha-Beta Pruning" if do_pruning else "Vanilla Minimax", 
        get_count()
    ))
    return winner

def play_against_ai(do_pruning):
    """Play an interactive game against the AI."""
    board = board_initialize(7, 6)
    print("Please choose who goes first: 1 for AI, 2 for You")
    try:
        first_player = int(input("Enter your choice: "))
    except ValueError:
        first_player = AI

    reset_count()
    while True:
        if first_player == AI:
            print("AI's turn")
            if do_pruning:
                col, _ = alpha_beta_pruning(board, 4, -math.inf, math.inf, True, first_player)
            else:
                col, _ = minimax(board, 4, True, first_player)
            
            drop_disc(board, col, first_player)
            print_board(board)
            
            if winning_move(board, first_player):
                print("AI wins!")
                break
            first_player = HUMAN
            
        else:
            print("Your turn.")
            try:
                col = int(input("Your choice (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
                
            if is_location_valid(board, col):
                drop_disc(board, col, first_player)
                print_board(board)
                
                if winning_move(board, first_player):
                    print("You win!")
                    break
            else:
                print("Invalid move. Please try again.")
                continue
            
            first_player = AI
            
        if is_full(board):
            print("It's a tie!")
            break
            
    print("Total nodes accessed: ", get_count())
