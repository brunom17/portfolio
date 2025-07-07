# 🛒 Online Shopping Intent Classifier

This project implements a **k-nearest neighbor classifier** to predict whether a user browsing an e-commerce website will complete a purchase during their session. The model is trained on user behavior data, such as page visit patterns and browser types, and evaluated using **sensitivity** and **specificity** metrics.

---

## 🎯 Features

- Parses and processes real session data from ~12,000 users.
- Trains a KNN classifier (k=1) using Scikit-learn.
- Computes:
  - **Sensitivity** (true positive rate)
  - **Specificity** (true negative rate)

---

## 🧠 Problem Overview

The classifier predicts the likelihood of purchase (`Revenue = TRUE`) based on session features like:

- Page visit counts and durations
- Bounce and exit rates
- Time of visit (month, weekend)
- Browser and traffic information
- Visitor type (returning or new)

---

## 📊 Dataset Details

Each session contains:

- 17 features as input **evidence**
- 1 output label (`Revenue`) indicating purchase (1) or not (0)

All categorical data is converted to numerical format:
- `Month` ➝ 0 (Jan) to 11 (Dec)
- `VisitorType` ➝ 1 (Returning_Visitor) or 0
- `Weekend` ➝ 1 if TRUE, else 0

---

## 🗂️ Project Structure

| File          | Description |
|---------------|-------------|
| `shopping.py` | Main script for data loading, training, prediction, and evaluation. |
| `shopping.csv`| Data file containing session-level user behavior and labels. |

---

## ⚙️ Functions

| Function       | Purpose |
|----------------|---------|
| `load_data()`  | Parses the CSV and returns evidence and labels. |
| `train_model()`| Trains a KNN model with `k=1`. |
| `evaluate()`   | Computes sensitivity and specificity from predictions. |

---

## ▶️ Running the Program

### Requirements

- Python 3.x
- scikit-learn

Install the dependency if needed:

```bash
pip install scikit-learn
```

### Usage

```bash
python shopping.py shopping.csv
```

### Sample Output

```text
Correct: 9124
Incorrect: 2673
True Positive Rate: 59.84%
True Negative Rate: 85.21%
```

---

## 🔎 Evaluation Metrics

- **Sensitivity**: Accuracy on users who did make a purchase.
- **Specificity**: Accuracy on users who did not make a purchase.

These give a more balanced view of model performance than raw accuracy.

---

## 🚀 Future Enhancements

- Hyperparameter tuning (e.g., vary `k`)
- Feature normalization or selection
- Try other models (SVM, Decision Trees, Random Forests)