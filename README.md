# Connect 4 AI: Minimax & Alpha-Beta Pruning (HKUST)

A structural implementation of a Connect 4 AI agent using adversarial search algorithms. This project was migrated from a Jupyter Notebook into a modular Python codebase, preserving the core game logic and heuristic evaluation techniques.

![Connect 4 Board](https://upload.wikimedia.org/wikipedia/commons/a/ad/Connect_Four.gif)

## 🎯 Features

- **Full Game Logic**: Traditional 7x6 Connect 4 board rules.
- **Minimax Algorithm**: A recursive decision-making search for optimal moves.
- **Alpha-Beta Pruning**: Highly optimized search that reduces child node exploration without changing the outcome.
- **Heuristic Evaluation**: Custom scoring function based on potential winning windows (horizontal, vertical, and diagonal).
- **Simulation Mode**: Run pre-defined human move sequences to compare algorithm efficiency.
- **Interactive Mode**: Play against the AI directly in the terminal.

## 🧠 AI Techniques

### Minimax Algorithm

The AI explores the game tree to a depth of 4 levels, alternating between maximizing its own score and minimizing the opponent's score.

### Alpha-Beta Pruning

An optimization that skips branches that cannot possibly influence the final decision, significantly improving performance.

## 📊 Performance Comparison

| Algorithm              | Nodes Visited | Efficiency Gain    |
| ---------------------- | ------------- | ------------------ |
| **Vanilla Minimax**    | 10,385        | -                  |
| **Alpha-Beta Pruning** | 4,700         | **~54% Reduction** |

_Note: Results are based on the standard simulation provided in `main.py`._

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- NumPy

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Connect4-Minimax-AlphaBeta-HKUST.git
cd Connect4-Minimax-AlphaBeta-HKUST

# Install dependencies
pip install numpy
```

### Usage

Run the main script to see the performance comparison:

```bash
python main.py
```

To play against the AI, uncomment the following line at the bottom of `main.py`:

```python
play_against_ai(do_pruning=True)
```

## 📁 Project Structure

- `src/board.py`: Board state, visualization, and hardware-like operations.
- `src/rules.py`: Winning conditions and terminal state detection.
- `src/evaluation.py`: Heuristic scoring logic.
- `src/minimax.py`: Implementation of search algorithms.
- `src/game.py`: Game runners and simulation controllers.
- `main.py`: Entry point for simulations and interactive play.

---
