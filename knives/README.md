# 🧠 Knights and Knaves: Logic Puzzle Solver

This project implements an AI system capable of solving **Knights and Knaves** logical puzzles using **propositional logic** and a **model-checking algorithm**. Inspired by Raymond Smullyan's famous puzzles, the AI deduces the identity (knight or knave) of each character based on their statements.

---

## 🎯 Features

- Encodes logical rules and character statements using propositional logic.
- Uses a model-checking engine to automatically deduce truths.
- Supports multi-character puzzles with nested logical implications.
- Demonstrates clear, structured AI reasoning for logic puzzles.

---

## 🧩 How the AI Works

The logic of the puzzles is formalized using **propositional logic**:

- **Symbols**: Represent statements like `A is a Knight`, `B is a Knave`, etc.
- **Connectives**: `And`, `Or`, `Not`, `Implication`, `Biconditional` are used to combine symbols.
- **Model Checking**: Exhaustively checks all truth assignments to determine if a sentence logically follows from the knowledge base.

Each puzzle is modeled by:
- Fundamental assumptions (each character is either a knight or a knave).
- Logical implications of what a character says, depending on their identity.

---

## 🗂️ Project Structure

| File         | Description |
|--------------|-------------|
| `logic.py`   | Contains classes to represent and evaluate propositional logic sentences. |
| `puzzle.py`  | Defines the puzzles, encodes logical rules, and runs the model-checker to solve them. |

---

## 🧠 Puzzle Overview

| Puzzle # | Description |
|----------|-------------|
| **0**    | A says “I am both a knight and a knave.” |
| **1**    | A says “We are both knaves.” B says nothing. |
| **2**    | A says “We are the same kind.” B says “We are of different kinds.” |
| **3**    | A makes a vague statement, B reports it and makes another claim, C makes a claim about A. |

Each puzzle demonstrates increasing complexity and deeper logical reasoning.

---

## ▶️ Running the Program

### Prerequisites

Ensure Python 3 is installed. No external libraries are required.

---

### Execution

Run the program with:

```bash
python puzzle.py
```

Expected output (example):

```text
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
...
```

Each line indicates what the model-checking algorithm was able to conclusively determine.

---

## 🔑 Logic Examples

Here’s how a sample statement is encoded:

> A says “I am both a knight and a knave.”

Translated into logic:

```python
Implication(AKnight, And(AKnight, AKnave))
Implication(AKnave, Not(And(AKnight, AKnave)))
```

This means: if A is a knight, the statement must be true; if A is a knave, the statement must be false.

---

## 🚀 Future Extensions

- Add support for custom puzzle input via text interface.
- Visualize the logical reasoning tree.
- Expand to include more complex logical connectives and quantifiers.