
# 👪 Heredity AI: Inferring Genetic Traits with Bayesian Networks

This project implements an AI system that uses **Bayesian inference** to determine the likelihood of individuals carrying a **mutated version of the GJB2 gene**, which is associated with hearing impairment. Given a dataset of individuals, including their parents and whether they exhibit a trait, the AI computes the probability distribution over their genetic makeup and traits.

---

## 🎯 Features

- Models **hidden genetic states** (0, 1, or 2 copies of the gene) and traits (True or False).
- Accounts for **parental inheritance** and **random mutation**.
- Computes **joint probabilities** for every possible genetic combination.
- **Normalizes** results to generate valid probability distributions.
- Supports **inference from partial data**, including unknown parental genes or traits.

---

## 🧠 How the AI Works

The AI uses a **Bayesian Network** to model each person’s gene and trait states. It considers:

- Gene inheritance from parents, following Mendelian genetics.
- Mutation probabilities.
- Trait expression probabilities based on gene count.

It calculates:

1. **Joint probability** for a complete hypothesis (gene & trait for all individuals).
2. **Updates** cumulative probabilities for each gene/trait configuration.
3. **Normalizes** the probabilities to ensure distributions sum to 1.

---

## 📁 Project Structure

| File           | Description |
|----------------|-------------|
| `heredity.py`  | Main program that loads the dataset, calculates probabilities using Bayesian inference, and prints final results. |
| `data/familyX.csv` | Example datasets including people, their parents, and observed traits. |

---

## 🔑 Key Functions in `heredity.py`

| Function           | Description |
|--------------------|-------------|
| `joint_probability()` | Computes the probability of a specific gene/trait configuration for all people. |
| `update()`         | Adds a joint probability to each individual's gene and trait distributions. |
| `normalize()`      | Adjusts all probability distributions to ensure they sum to 1. |
| `powerset()`       | Generates all subsets of a set (used to explore all combinations). |

---

## ▶️ Getting Started

### Prerequisites

Ensure Python 3 is installed.

---

### Running the Program

To run the model on a dataset:

```bash
python heredity.py data/family0.csv
```

You’ll get output like:

```
Harry:
  Gene:
    2: 0.0031
    1: 0.0486
    0: 0.9483
  Trait:
    True: 0.1873
    False: 0.8127
```

---

## 📊 Example: How Probability is Computed

Given:
- `Harry` has one gene.
- `James` has two genes and the trait.
- `Lily` has zero genes and no trait.

Joint probability is calculated by multiplying:
- Gene inheritance likelihood.
- Trait expression based on gene count.

Including mutation probabilities, the final joint probability is:

```text
P = P(Lily's genes & trait) × P(James's genes & trait) × P(Harry's genes & trait)
```

---

## 📌 Notes

- The model is based on CS50 AI’s heredity project.
- Mutation and trait probabilities are adjustable via `PROBS`.
- Works well with small datasets; larger families increase computation time.

---

## 🚀 Future Enhancements

- Add graphical visualization of probability distributions.
- Support for multiple traits or polygenic models.
- Optimization using memoization or probabilistic programming libraries.

