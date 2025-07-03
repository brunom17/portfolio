
# ✏️ Crossword Puzzle Generator with CSP

This project implements an AI that generates **crossword puzzles** using **Constraint Satisfaction Problems (CSP)**. Given a puzzle structure and a list of words, the AI uses constraint propagation, heuristics, and backtracking to fill in the crossword with valid, non-repeating words that satisfy all constraints.

---

## 🎯 Features

- Solves crossword puzzles using **backtracking search** with heuristics.
- Enforces **node** and **arc consistency** using **AC-3** algorithm.
- Applies **Minimum Remaining Values** and **Degree heuristics** for variable selection.
- Implements **Least Constraining Value** ordering for domain values.
- Supports puzzle visualization and image export (using Pillow).

---

## 🧠 How the AI Works

The crossword generation is treated as a CSP:

- **Variables**: Sequences in the crossword (across/down with a specific length).
- **Domains**: List of words matching each variable’s length.
- **Unary Constraints**: Word length must match variable length.
- **Binary Constraints**: Overlapping characters between variables must match.
- **Global Constraint**: No repeated words allowed in the puzzle.

The solver:
1. Removes values violating unary constraints.
2. Enforces binary constraints with **AC-3** to prune the domains.
3. Uses **backtracking** to find a consistent assignment for all variables.

---

## 🗂️ Project Structure

| File           | Description |
|----------------|-------------|
| `crossword.py` | Contains the data structures for variables and the crossword grid. |
| `generate.py`  | The CSP solver: enforces consistency, applies heuristics, and generates the final puzzle. |
| `data/`        | Contains puzzle structures and word lists. |

---

## 🔑 Key Functions in `generate.py`

| Function                      | Description |
|-------------------------------|-------------|
| `enforce_node_consistency()`  | Removes domain values that violate word length constraints. |
| `revise(x, y)`                | Makes variable `x` arc-consistent with `y`. |
| `ac3()`                       | Runs the AC-3 algorithm to enforce arc consistency. |
| `assignment_complete()`       | Checks if the assignment is complete. |
| `consistent()`                | Validates if current assignment meets all constraints. |
| `order_domain_values(var)`    | Returns domain values ordered by the least-constraining heuristic. |
| `select_unassigned_variable()`| Chooses an unassigned variable using MRV and degree heuristics. |
| `backtrack()`                 | Uses backtracking search to complete the assignment. |

---

## ▶️ Getting Started

### Prerequisites

Install Python 3 and Pillow for image output:

```bash
pip install pillow
```

---

### Running the Program

To generate a crossword:

```bash
python generate.py data/structure1.txt data/words1.txt
```

To save the result as an image:

```bash
python generate.py data/structure1.txt data/words1.txt output.png
```

---

## 📝 Notes

- Input structure files define where letters should be placed using `_`.
- The AI may not always find a solution if the word list is too limited.
- Intermediate steps use arc consistency and heuristic ordering to optimize search.

---

## 🧩 Example Heuristics

- **MRV**: Choose the variable with the fewest legal words.
- **Degree**: If tied, choose the variable with the most neighbors.
- **LCV**: Prefer words that rule out the fewest options for neighbors.

---

## 🚀 Future Improvements

- Support symmetric puzzles or themes.
- Integrate GUI for manual editing.
- Improve performance with forward-checking or stochastic search.
