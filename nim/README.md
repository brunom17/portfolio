# 🎮 Nim Game AI with Q-Learning

This project implements an AI to play the game **Nim** using **Q-learning**, a type of reinforcement learning. The AI learns optimal strategies by playing against itself thousands of times and improves over time.

---

## 🎯 Features

- Learns to play Nim optimally via self-play using Q-learning.
- Implements an epsilon-greedy strategy for exploration vs. exploitation.
- Fully playable against a human in the terminal.
- Adjustable training episodes and learning parameters (`alpha`, `epsilon`).

---

## 🧠 Game Description

**Nim** is a mathematical game of strategy. Players take turns removing one or more objects from a pile. The player forced to take the last object **loses**.

- **State**: A list representing pile sizes, e.g., `[1, 3, 5, 7]`.
- **Action**: A tuple `(i, j)` meaning remove `j` objects from pile `i`.

---

## 📘 Q-Learning Overview

The AI maintains a **Q-value** table mapping `(state, action)` pairs to learned reward values.

**Key Concepts**:

- `get_q_value(state, action)`: Returns learned value for a state-action.
- `update_q_value(...)`: Applies the Q-learning formula.
- `best_future_reward(state)`: Chooses the best known future reward.
- `choose_action(state)`: Chooses an action (greedily or randomly with epsilon).

**Q-learning update formula**:

```
Q(s, a) <- old_q + alpha * (reward + future_rewards - old_q)
```

---

## 🗂️ Project Structure

| File       | Description |
|------------|-------------|
| `nim.py`   | Core game logic, AI class, training and play functions. |
| `play.py`  | Runs training and starts a game against the AI. |

---

## ▶️ Getting Started

### Requirements

- Python 3.x (no additional libraries needed)

---

### Training the AI

Train the AI with a specified number of self-play games (e.g., 10,000):

```bash
python play.py
```

During training, you'll see:

```text
Playing training game 1
Playing training game 2
...
Done training
```

---

### Playing Against the AI

After training, the game starts:

```text
Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

Your Turn
Choose Pile: 2
Choose Count: 3
...
```

The AI will respond and the game continues until one player wins.

---

## 🚀 Future Improvements

- Save/load trained Q-tables to skip retraining.
- Add GUI or web interface for easier play.
- Support variable number of piles and initial configurations.