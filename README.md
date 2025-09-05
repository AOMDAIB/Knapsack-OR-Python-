# Knapsack-OR-Python-
One of the most widely studied optimization problems in computer science and operations research is the knapsack problem.  It entails choosing a group of objects with set weights and values in order to maximize the overall value while staying within a given capacity.


## Requirements
- Python 3.x
- OR-Tools: Install via `pip install ortools`

## How to Run
1. Save the script as `knapsack_solver.py`.
2. Open a terminal in the script's directory.
3. Run: `python knapsack_solver.py`

The script will output the total value, total weight, packed items, and their weights.

## Code Overview
- **Values**: Array of item values [90, 83, 59, 130, 187, 67, 230, 52, 93, 125, 98]
- **Weights**: Array of item weights [[7, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18]]
- **Capacity**: Knapsack can hold up to 350 units of weight.
- Uses branch-and-bound solver for optimal solution.
