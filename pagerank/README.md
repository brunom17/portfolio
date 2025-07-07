# 🔗 PageRank Algorithm: Web Page Importance Estimator

This project implements the **PageRank** algorithm to estimate the importance of web pages based on their hyperlink structure, mimicking part of how search engines like Google rank results.

---

## 🎯 Features

- Implements **two PageRank estimation methods**:
  - **Sampling-based** random surfer model.
  - **Iterative formula**-based method.
- Handles disconnected and dangling pages properly.
- Based on real-world web structure and probabilistic models.

---

## 🌐 PageRank Overview

**PageRank** is a probability distribution used to represent the likelihood that a person randomly clicking on links will arrive at any particular page.

- Important pages are those that are **linked to by other important pages**.
- The model uses a **damping factor** (typically 0.85) to simulate random jumps.

Two approaches are implemented:

### 📊 1. Sampling

Simulates a **random surfer** that:
- Starts on a random page.
- At each step, follows a link with probability `d`, or jumps to any page with `1 - d`.

### ♻️ 2. Iteration

Applies the PageRank formula repeatedly:
```
PR(p) = (1 - d) / N + d * Σ[PR(i) / NumLinks(i)]
```
Where:
- `d` is the damping factor.
- `N` is the total number of pages.
- The summation is over all pages `i` that link to page `p`.

---

## 🗂️ Project Structure

| File         | Description |
|--------------|-------------|
| `pagerank.py` | Core logic for crawling pages, computing PageRank via sampling and iteration. |
| `corpus/`     | Directory containing example HTML files to process. |

---

## ⚙️ Functions

| Function             | Purpose |
|----------------------|---------|
| `crawl(directory)`   | Parses HTML files and builds the link structure (corpus). |
| `transition_model()` | Builds a probability distribution for next pages. |
| `sample_pagerank()`  | Estimates PageRank by sampling N pages. |
| `iterate_pagerank()` | Iteratively computes PageRank values until convergence. |

---

## ▶️ Running the Program

### Requirements

- Python 3.x (no external libraries required)

### Usage

Run the script with a corpus folder:

```bash
python pagerank.py corpus
```

Example output:

```text
PageRank Results from Sampling (n = 10000)
  1.html: 0.2187
  2.html: 0.4073
  3.html: 0.3740

PageRank Results from Iteration
  1.html: 0.2198
  2.html: 0.4055
  3.html: 0.3747
```

---

## 📌 Notes

- If a page has no outbound links, it's treated as linking to **all** pages.
- Both methods normalize final ranks so they sum to 1.
- Iteration stops when values change less than `0.001`.

---

## 🚀 Future Enhancements

- Visualize page link graphs and rank heatmaps.
- Integrate with real web crawler tools.
- Apply to academic citation networks or social graphs.