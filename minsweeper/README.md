
# 🧠 Minesweeper AI

This project implements a playable version of **Minesweeper** along with an **AI agent** that can play the game logically by applying **propositional logic** and inference-based reasoning. The AI attempts to flag all mines without triggering any, using a knowledge base of logical sentences and inference techniques.

Built using **Python** and **Pygame**, this project demonstrates the power of logical reasoning in a real-time game scenario.

---

## 🎯 Features

- Classic Minesweeper gameplay with an 8x8 grid and 8 hidden mines.
- Play manually or let the AI play for you with the “AI Move” button.
- Visual interface built with Pygame.
- AI infers safe moves and mines using a propositional logic-based knowledge base.
- AI keeps learning and updating its knowledge to make smarter decisions over time.

---

## 🧠 How the AI Works

The AI represents its knowledge using sentences of the form:

```python
{cell1, cell2, ..., cellN} = count
```

This means exactly `count` of those `N` cells contain mines. From this representation, the AI can:

- Identify **safe** cells when `count = 0`.
- Identify **mine** cells when `count == len(cells)`.
- Use **inference by subset**: if one sentence is a subset of another, new knowledge can be derived.

The AI updates its knowledge base dynamically as new cells are revealed and new inferences are made.

---

## 🗂️ Project Structure

| File           | Description |
|----------------|-------------|
| `minesweeper.py` | Contains all the core game logic, propositional logic representation, and AI reasoning system. |
| `runner.py`      | Handles the graphical interface using Pygame and allows you to play manually or with the AI. |

---

## 🔑 Key Classes and Functions

### `Minesweeper` (in `minesweeper.py`)
- Creates the game board and places mines.
- Calculates the number of neighboring mines for a cell.
- Checks for a win condition.

### `Sentence`
- Represents a logical sentence in the form `{cells} = count`.
- `known_mines()` and `known_safes()` identify certain mines or safe cells.
- `mark_mine()` and `mark_safe()` update the sentence when new information is learned.

### `MinesweeperAI`
- Maintains sets of known `mines`, `safes`, and all `moves_made`.
- Builds and updates a list of `Sentence` objects (`knowledge`) to reason about the board.
- Key methods:
  - `add_knowledge(cell, count)`: Adds a new sentence and updates knowledge.
  - `make_safe_move()`: Returns a known safe cell to click.
  - `make_random_move()`: Chooses a random unexplored cell that’s not known to be a mine.

---

## ▶️ Getting Started

### Prerequisites

Make sure Python 3 and Pygame are installed:

```bash
pip install pygame
```

---

### Running the Game

To launch the game with the graphical interface:

```bash
python runner.py
```

You can click to play manually or use the **AI Move** button to let the AI play.

---

## 📝 Notes

- The AI may not always win since some situations require guessing (i.e., not enough logical information is available).
- The AI automatically updates its knowledge base with every new move, and can infer new information even several steps later.
- The project showcases the usefulness of logical inference and knowledge representation in uncertain environments.

---

## 🚀 Future Improvements

- Add support for different difficulty levels and board sizes.
- Implement probabilistic reasoning for better random move selection.
- Visualize the AI’s internal knowledge for educational insight.
