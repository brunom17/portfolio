# Tic-Tac-Toe AI with Minimax Algorithm

This project implements a complete Tic-Tac-Toe game where you can play against an unbeatable AI powered by the **Minimax algorithm**. The game comes with a graphical interface built using **Pygame**, allowing for an interactive experience.

## 🎮 Features

- Two-player mode: You can choose to play as **X** or **O**.
- The AI uses **Minimax** to make optimal decisions.
- Graphical board display built with **Pygame**.
- Full game logic: detecting legal moves, terminal states, winners, and calculating utility values.
- Clean separation between game logic (`tictactoe.py`) and UI logic (`runner.py`).

## 🧠 How the AI Works

The AI always plays optimally using the Minimax algorithm. This means:
- It explores all possible future game states.
- It assumes the opponent will also play optimally.
- It chooses the move that maximizes its chances of winning (or minimizing losses).
- As a result, **you can never beat the AI**—at best, you can tie.

## 📁 Project Structure

- `tictactoe.py`: Implements the game logic and the Minimax decision-making.
- `runner.py`: Runs the Pygame interface and lets you play against the AI.

## 🛠️ Key Functions in `tictactoe.py`

| Function       | Description |
|----------------|-------------|
| `initial_state()` | Returns the starting empty board. |
| `player(board)` | Determines whose turn it is (X or O). |
| `actions(board)` | Returns a set of all available moves. |
| `result(board, action)` | Returns a new board with the move applied. |
| `winner(board)` | Checks for a winner (X, O, or None). |
| `terminal(board)` | Returns `True` if the game is over. |
| `utility(board)` | Returns 1 if X wins, -1 if O wins, 0 for a tie. |
| `minimax(board)` | Returns the optimal move using the Minimax algorithm. |

## ▶️ Getting Started

### Prerequisites

Make sure you have Python 3 installed, along with the Pygame library:

```bash
pip install pygame
Running the Game
Simply run:

bash
Copy
Edit
python runner.py
A window will open where you can select your player and start playing.

📝 Notes
The AI uses recursion to evaluate all possible moves, which is feasible in Tic-Tac-Toe due to the small board size.

The original board is never mutated—new boards are created for each hypothetical move.

The project could be expanded to include alpha-beta pruning to improve efficiency.

