
# 🎬 Degrees of Separation: Actor Connection Finder

This project implements a search-based AI that identifies the **shortest path between two actors** based on movies they've starred in together. Inspired by the "Six Degrees of Kevin Bacon" game, the program uses **Breadth-First Search (BFS)** to compute degrees of separation between actors in the film industry.

---

## 🎯 Features

- Computes the shortest path of connections between two actors using BFS.
- Uses real-world IMDb-style datasets with actors, movies, and star relationships.
- Handles ambiguous names and duplicate actors.
- Supports large datasets with thousands of actors and films.
- Explains each step in the path clearly with movie titles and actor names.

---

## 🧠 How the AI Works

The problem is modeled as a graph search:

- **States**: Individual actors (by ID).
- **Actions**: Movies that connect two actors.
- **Goal**: A path from one actor to another through shared movies.

The **Breadth-First Search** algorithm ensures the shortest connection path is found. The program explores all neighbors (i.e., co-stars) level-by-level until the target actor is reached.

---

## 🗂️ Project Structure

| File           | Description |
|----------------|-------------|
| `degrees.py`   | Core logic for loading data, handling input, and finding shortest path between actors. |
| `util.py`      | Contains data structures (Node, StackFrontier, QueueFrontier) used in search. |
| `data/`        | Contains CSV files for people, movies, and star relationships. |
| `large/` and `small/` | Two versions of the dataset for performance testing and quick debugging. |

---

## 🔑 Key Functions in `degrees.py`

| Function             | Description |
|----------------------|-------------|
| `load_data()`        | Loads all actor and movie data into memory from CSV files. |
| `shortest_path()`    | Uses BFS to find the shortest connection path between two actors. |
| `neighbors_for_person()` | Returns all (movie_id, person_id) pairs who co-starred with a given person. |
| `person_id_for_name()`   | Resolves actor name to a unique IMDb-style ID, with support for ambiguities. |

---

## ▶️ Getting Started

### Prerequisites

Ensure Python 3 is installed. No additional libraries are required.

---

### Running the Program

Run the main program and enter two actor names:

```bash
python degrees.py
```

You will be prompted:

```text
Name: Jennifer Lawrence
Name: Tom Hanks
2 degrees of separation.
1: Jennifer Lawrence and Kevin Bacon starred in X-Men: First Class
2: Kevin Bacon and Tom Hanks starred in Apollo 13
```

You can also use the smaller dataset for quick testing:

```bash
python degrees.py small
```

---

## 📝 Notes

- Uses a `QueueFrontier` to enforce BFS logic.
- Tracks explored states to prevent cycles and redundant exploration.
- Returns `None` if no connection exists between the given actors.
- Automatically handles actors with multiple entries (same name, different ID).

---

## 🚀 Future Improvements

- Add support for weighted graphs (e.g., based on collaboration frequency).
- Visualize the actor network using graph libraries like NetworkX.
- Extend to include director and writer relationships for broader linkage.

