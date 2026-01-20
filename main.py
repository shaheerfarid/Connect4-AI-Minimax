from src.game import game_check, play_against_ai
from src.board import AI

if __name__ == "__main__":
        # Predefined human moves for simulation
        test_human_array = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]

        print("--- Running Node Comparison Simulation ---")
        winner_vanilla = game_check(test_human_array, AI, do_pruning=False)
        print(f"Vanilla Minimax Winner: {winner_vanilla}")
        
        print("\n--- Running Alpha-Beta Pruning Simulation ---")
        winner_ab = game_check(test_human_array, AI, do_pruning=True)
        print(f"Alpha-Beta Pruning Winner: {winner_ab}")

        print("\n--- Project Migrated Successfully! ---")
    # Uncomment the line below to play interactively:
    # play_against_ai(do_pruning=True)
