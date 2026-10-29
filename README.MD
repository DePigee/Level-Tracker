---

# CS 111: Introduction to Programming
## Assignment 1: The Level Tracker

## Objective

Practice variables, functions, loops, lists, dictionaries, sets, comparisons, and basic error handling by building a small tool that tracks player XP and assigns levels.

## The Scenario

A small game studio exported player data from its servers. The data is messy:

1. Some players appear more than once.
2. Some XP entries are bad text instead of numbers.
3. Some players have no XP entries at all.

Your job is to write `leveltracker.py`, which cleans the data, totals each player's XP, assigns a level, and prints a report.

## Input Data

Paste this at the top of your file:

```python
PLAYERS = [
    {"player_id": "P1", "name": "Zara", "xp": [120, 80, 150]},
    {"player_id": "P2", "name": "Milo", "xp": [200, "lots", 90]},
    {"player_id": "P3", "name": "Juno", "xp": [40, 30]},
    {"player_id": "P1", "name": "Zara", "xp": [120, 80, 150]},  # Duplicate
    {"player_id": "P4", "name": "Kai", "xp": []},               # No XP
    {"player_id": "P5", "name": "Rhea", "xp": [500, 450, 300]},
]
```

## Functional Requirements

Write each of these as its own function.

### 1. `remove_duplicates(players)`
- Accepts the raw list of players.
- Returns a new list in which every `player_id` appears only once.
- Hint: use a set to track IDs you've already seen.

### 2. `total_xp(xp_list)`
- Accepts one player's list of XP values (not the whole player).
- Returns the sum of the valid numbers.
- Use `try...except` to skip any value that can't be converted to a number.
- If there are no valid values, return `0`.

### 3. `get_level(xp)`

| Total XP | Level |
|---|---|
| 1000 or more | Master |
| 500 to 999 | Expert |
| 200 to 499 | Skilled |
| 1 to 199 | Beginner |
| 0 | Unranked |

### 4. `print_report(players)`
- Loops through the cleaned list.
- Calls `total_xp` and `get_level` for each player.
- Prints the table below.

### 5. Bonus: type hints
Add type hints to every function (for example, parameters and return types).

## Expected Output

```
==============================
PLAYER LEVEL REPORT
==============================
ID    NAME     XP     LEVEL
------------------------------
P1    Zara     350    Skilled
P2    Milo     290    Skilled
P3    Juno     70     Beginner
P4    Kai      0      Unranked
P5    Rhea     1250   Master
------------------------------
Total Players: 5
==============================
```

## Submission Guidelines

1. Make a Git repo and commit after each function (for example, `feat: add remove_duplicates`).
2. Open a pull request per function, as you did before.
3. When your output matches exactly, paste your code for review.

---
