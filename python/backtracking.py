def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:  # Check column
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)]:  # Check left diagonal
            return False
        if col + (row - i) < n and board[i][col + (row - i)]:  # Check right diagonal
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            solve_n_queens(board, row + 1, n)
            board[row][col] = False  # Backtrack

def n_queens(n):
    board = [[False] * n for _ in range(n)]
    solve_n_queens(board, 0, n)

# Example usage
n_queens(4)  # Solves 4-Queens problem
