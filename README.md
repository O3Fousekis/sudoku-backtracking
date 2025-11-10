Overview

For the creation of the program, the auxiliary function random was used to initialize the board and then solve it.
Within the program, several functions were implemented, each serving a specific purpose.

Functions
valid(board, row, col, num)

This function checks, starting from the top-left element of each subgrid, whether the value being considered for assignment is valid.
This is achieved based on the rules of Sudoku — meaning that the same number must not appear more than once in any row, column, or subgrid.

hasEmptyCells(board)

This function is used during the board-solving process, as it checks whether the board contains any empty (zero) cells.

init_board(board, amount)

This function initializes the board with zeros and then fills in the first values based on the user’s input.

Steps:

The cell positions are collected into a list.

The list is shuffled to ensure an even distribution of numbers.

A loop runs until the number of initialized cells reaches the user-specified amount.

Within this loop:

Each assignment is checked for validity.

If valid, a random value is assigned to the corresponding cell.

Otherwise, another random value is chosen and rechecked.

backtracking(board)

This function performs the solving of the initialized board.

Process:

It first checks whether the board is full.

Since the function is recursive, if the board is full, it returns True.

Otherwise, it selects the first empty cell and examines the possible values it can take.

Values already existing in the same row, column, or subgrid are excluded using the valid function.

This continues until the entire 9×9 board is filled.

If a randomly assigned value does not satisfy the conditions of valid, the cell’s value is reset to 0 and re-evaluated.

Algorithm Description

The program is implemented based on the backtracking algorithm:

For each cell, a possible value is tested.

If the value is not valid, the cell’s value is reset and rechecked.

This process is repeated for all cells until the initial 9×9 board is fully completed and deemed solved.

Input Validation and Initialization

After defining the functions, an input validation check ensures the proper initialization of the board with values.

Once the input passes validation:

The 9×9 board is initialized with a number of filled cells based on the user’s input.

It should be noted that for large values (>30), the program may take a long time to initialize or solve the board, due to:

The limited number of possible combinations.

The random selection of numbers during each iteration.

Additionally, there is a possibility that the function may fail to find a valid solution for the board.
