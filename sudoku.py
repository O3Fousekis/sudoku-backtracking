import random

board = [[0 for i in range(9)] for j in range(9)] # initializing board

def valid(board, row, col, num): # used for the constraints of the numbers

    # checks if a number already exists in the row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]: 
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3) # start corner of every 3x3 subtable
    for i in range(3):
        for j in range(3):

            # checks if the number already exists in the 3x3 subtable
            if board[start_row + i][start_col + j] == num:
                return False
            
    return True

def hasEmptyCells(board): # used for checking if the board has empty cells, used for solving the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def init_board(board, amount): # board initialization

    for i in range(9):
        for j in range(9):
            board[i][j] = 0

    # creates a list of cells, and shuffles it for random number generation
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    # fills the cells until the user input value is reached.
    for k in range(amount):
        i, j = cells[k]
        num = random.randint(1, 9)
        while not valid(board, i, j, num):
            num = random.randint(1, 9)
        board[i][j] = num 

def backtracking(board): # using backtracking for solving the sudoku board
    empty_cell = hasEmptyCells(board)

    if not empty_cell: # board is full
        return True
    
    # marks the coordinates of the empty cell and takes a sample of the possible numbers
    row, col = empty_cell
    # the possible numbers are the numbers that aren't used in the row, column or subtable, so it dynamically updates based on every marked cell.
    possible_numbers = [num for num in range(1, 10) if valid(board, row, col, num)]
    random.shuffle(possible_numbers)

    for num in possible_numbers:
        board[row][col] = num # appends the number to the marked coordinates

        if backtracking(board): # using recursion until the board is filled.
            return True

        # if the assignment made to the cell didn't work, it resets the cell value and tries again.
    board[row][col] = 0
    return False

# checking if the input value is between 1-81.
while True:
    user_in = input("Input the amount of cells to be initialized: ")

    try:
        in_value = int(user_in)
        if 1 <= in_value <= 81:
            break
        else:
            print("Value must be between 1 and 81.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


init_board(board, in_value)
print("Initial board state:")

for row in board: # prints the initial board
    print(row)

# uses backtracking until the board is filled, then prints it
print("Solving the board using the backtracking method.")
if backtracking(board):
    print("Board solved:")
    for row in board:
        print(row)
else:
    print("No solution found.")