
# 🧠 Natural Language Parser with CFG

This project implements a **Natural Language Parser** using **Context-Free Grammar (CFG)** and **NLTK**. It parses English sentences, determines their grammatical structure, and extracts **noun phrase chunks**, aiding in understanding and information extraction.

---

## 🎯 Features

- Uses **Context-Free Grammar rules** to parse sentences.
- Identifies and displays complete **parse trees**.
- Extracts minimal **noun phrase chunks** from syntax trees.
- Supports complex phrases with determiners, adjectives, prepositions, adverbs, and conjunctions.

---

## 🧠 How the Parser Works

The parser is built using NLTK's `ChartParser` and a defined grammar:

- **Terminals**: Words categorized into parts of speech (nouns, verbs, adjectives, etc.).
- **Nonterminals**: Grammar rules to generate full sentences (`S`), noun phrases (`NP`), verb phrases (`VP`), prepositional phrases (`PP`), etc.

The sentence is first tokenized and preprocessed:
- Converted to lowercase.
- Filtered to exclude non-alphabetic tokens.

It is then parsed using the defined grammar, and the resulting trees are analyzed to extract noun phrase chunks.

---

## 🗂️ Project Structure

| File         | Description |
|--------------|-------------|
| `parser.py`  | The main parser: contains grammar rules, preprocessing, parse tree generation, and noun phrase extraction. |
| `sentences/` | Folder containing sample input sentences (e.g., `1.txt`, `2.txt`, etc.) |

---

## 🔑 Key Components

| Component         | Description |
|------------------|-------------|
| `TERMINALS`      | Lists possible terminal words by part-of-speech. |
| `NONTERMINALS`   | Grammar rules for parsing full sentence structure. |
| `preprocess()`   | Tokenizes and cleans the sentence. |
| `np_chunk()`     | Extracts minimal noun phrase chunks (NPs without nested NPs). |

---

## ▶️ Getting Started

### Prerequisites

Install Python 3 and NLTK:

```bash
pip install nltk
```

If `punkt` is not available locally, download it (for tokenization):

```python
import nltk
nltk.download('punkt')
```

---

### Running the Parser

To parse a sentence from file:

```bash
python parser.py sentences/1.txt
```

Or enter one interactively:

```bash
python parser.py
Sentence: Holmes sat in the red armchair.
```

---

## 🧪 Example Output

```
         S
     ____|___
    NP      VP
    |     ___|___
    N    V      PP
    |    |     __|___
 Holmes sat  P      NP
             |    __|___
            in  Det     N
                 |      |
                the  armchair

Noun Phrase Chunks
Holmes
the armchair
```

---

## 🚀 Future Improvements

- Support probabilistic parsing or semantic role labeling.
- Extend grammar to support questions and passive voice.
- Visualize noun phrase chunks directly in the tree.

---

## 📝 Notes

- A **noun phrase chunk** is a minimal NP subtree not containing any other NP.
- Grammar has been carefully crafted to avoid over- and under-generation.
- Parser handles nested structures and conjunctions.
