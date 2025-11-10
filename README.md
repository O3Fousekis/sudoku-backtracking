# Sudoku Solver Program Documentation

## Overview
The program uses the auxiliary function `random` to initialize the board and then solve it. Several functions are implemented, each serving a specific purpose in the process of filling and solving a Sudoku board.

---

## Functions

### `valid(board, row, col, num)`
This function checks whether a value can be assigned to a specific cell without violating Sudoku rules. It ensures that the same number does not appear more than once in any **row**, **column**, or **3×3 subgrid**.

---

### `hasEmptyCells(board)`
Checks whether the board contains any empty (zero) cells. This is used during the solving process to identify cells that still need a value.

---

### `init_board(board, amount)`
Initializes the board with zeros and then fills in the first `amount` of cells randomly, ensuring that each assignment is valid. The process involves:

- Collecting all cell positions into a list and shuffling them to ensure even distribution.  
- Filling cells one by one with random values while checking validity.  
- Reassigning random values if the selected number does not satisfy the Sudoku rules.  

---

### `backtracking(board)`
Solves the Sudoku board using a recursive **backtracking algorithm**. The process:

- Checks if the board is full. If so, the solution is complete.  
- Selects the first empty cell and tries all possible numbers that are valid.  
- If no valid number can be placed, the cell is reset to zero and re-evaluated.  
- Continues recursively until the entire **9×9 board** is filled and solved.

---

## Algorithm Description
The program is based on the **backtracking algorithm**:

- For each empty cell, a candidate value is tested.  
- If the value is invalid, the cell is reset and another candidate is tried.  
- This continues until all cells are correctly filled.  

This guarantees that, if a solution exists, the board will be solved correctly.

---

## Input Validation and Initialization
- Input is first validated to ensure correctness.  
- The board is then initialized with the number of filled cells specified by the user.  

**Notes:**

- For large initial numbers of cells (>30), the program may take longer to initialize or solve due to limited combinations and repeated random attempts.  
- There is a possibility that the program may not find a valid solution for certain configurations.
