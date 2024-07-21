import random

# Function to initialize the game board
def initialize_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines_placed = 0
    while mines_placed < num_mines:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if board[x][y] != '*':
            board[x][y] = '*'
            mines_placed += 1
    return board

# Function to print the board
def print_board(board):
    size = len(board)
    print("   ", end="")
    for i in range(size):
        print(f" {i}", end="")
    print("\n  +", end="")
    print("--" * size + "-")
    for i in range(size):
        print(f"{i} |", end="")
        for j in range(size):
            print(f" {board[i][j]}", end="")
        print()

# Function to count adjacent mines
def count_adjacent_mines(board, x, y):
    size = len(board)
    count = 0
    for i in range(max(0, x - 1), min(size, x + 2)):
        for j in range(max(0, y - 1), min(size, y + 2)):
            if (i != x or j != y) and board[i][j] == '*':
                count += 1
    return count

# Function to reveal a cell
def reveal_cell(board, x, y):
    if board[x][y] == '*':
        return False
    elif board[x][y] == ' ':
        board[x][y] = str(count_adjacent_mines(board, x, y))
        if board[x][y] == '0':
            for i in range(max(0, x - 1), min(len(board), x + 2)):
                for j in range(max(0, y - 1), min(len(board), y + 2)):
                    if (i != x or j != y) and board[i][j] == ' ':
                        reveal_cell(board, i, j)
    return True

# Main function to run the game
def minesweeper(size=5, num_mines=5):
    board = initialize_board(size, num_mines)
    print_board(board)

    while True:
        try:
            x = int(input("Enter row number to reveal: "))
            y = int(input("Enter column number to reveal: "))
            if x < 0 or x >= size or y < 0 or y >= size:
                print("Invalid input. Please enter valid coordinates.")
                continue
            if not reveal_cell(board, x, y):
                print_board(board)
                print("Game Over! You hit a mine.")
                break
            print_board(board)
            print("Congratulations! You are safe.")
        except ValueError:
            print("Invalid input. Please enter valid coordinates.")
            continue

# Example usage
if __name__ == "__main__":
    size = 5  # Change the board size here
    num_mines = 5  # Change the number of mines here
    minesweeper(size, num_mines)
