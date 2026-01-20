# Connect 4 AI: Minimax & Alpha-Beta Pruning

A high-performance Connect 4 AI agent implementing adversarial search algorithms. This repository contains a modular Python implementation of the Minimax algorithm with Alpha-Beta Pruning, offering a significant reduction in search complexity while maintaining optimal decision-making.

![Connect 4 Board](https://upload.wikimedia.org/wikipedia/commons/a/ad/Connect_Four.gif)

## 🎯 Features

- **Modular Architecture**: Separate modules for board management, game rules, heuristic evaluation, and search algorithms.
- **Advanced AI**: Uses Minimax search with a configurable depth and Alpha-Beta Pruning for efficiency.
- **Heuristic Evaluation**: Intelligent scoring function that evaluates board states based on potential Winning Windows.
- **Interactive Gameplay**: Play against the AI directly in your terminal.
- **Simulation Tools**: Built-in comparison tools to analyze the performance of Vanilla Minimax vs. Alpha-Beta Pruning.

## 📊 Search Efficiency

The AI demonstrates the power of Alpha-Beta Pruning by reducing the state-space exploration significantly:

| Algorithm              | Nodes Visited (Simulation) | Efficiency Gain    |
| ---------------------- | -------------------------- | ------------------ |
| **Vanilla Minimax**    | 10,385                     | -                  |
| **Alpha-Beta Pruning** | 4,700                      | **~54% Reduction** |

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- NumPy

### Installation

```bash
# Clone the repository
git clone https://github.com/shaheerfarid/Connect4-AI-Minimax.git
cd Connect4-AI-Minimax

# Install dependencies
pip install numpy
```

### Running the Project

To run the performance simulation and verify the AI logic:

```bash
python main.py
```

To play an interactive game against the AI, ensure the following line is active in `main.py`:

```python
play_against_ai(do_pruning=True)
```

## 📁 Project Structure

- `src/board.py`: Board state management and visualization.
- `src/rules.py`: Win conditions and game logic.
- `src/evaluation.py`: Heuristic position scoring.
- `src/minimax.py`: Minimax and Alpha-Beta Pruning implementations.
- `src/game.py`: Interactive and simulation game loops.
- `main.py`: Project entry point.

---
