import time

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    return True

def solve_nqueens_backtracking(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nqueens_backtracking(board, col + 1, n):
                return True
            board[i][col] = 0
    
    return False

def solve_nqueens_branch_and_bound(n):
    def solve(col, left_diag, right_diag, rows):
        if col == n:
            return True
        
        for i in range(n):
            if not rows[i] and not left_diag[i + col] and not right_diag[i - col + n - 1]:
                board[i][col] = 1
                rows[i] = left_diag[i + col] = right_diag[i - col + n - 1] = True
                
                if solve(col + 1, left_diag, right_diag, rows):
                    return True
                
                board[i][col] = 0
                rows[i] = left_diag[i + col] = right_diag[i - col + n - 1] = False
        
        return False
    
    board = [[0] * n for _ in range(n)]
    left_diag = [False] * (2 * n - 1)
    right_diag = [False] * (2 * n - 1)
    rows = [False] * n
    
    if solve(0, left_diag, right_diag, rows):
        return board
    return None

def print_board(board):
    if board:
        for row in board:
            print(" ".join("Q" if x else "." for x in row))
    else:
        print("No solution found.")

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    print("Solving using Backtracking...")
    board = [[0] * n for _ in range(n)]
    start_time = time.time()
    if solve_nqueens_backtracking(board, 0, n):
        print_board(board)
    else:
        print("No solution found.")
    print("Time taken (Backtracking):", time.time() - start_time, "seconds")
    
    print("\nSolving using Branch and Bound...")
    start_time = time.time()
    board = solve_nqueens_branch_and_bound(n)
    print_board(board)
    print("Time taken (Branch and Bound):", time.time() - start_time, "seconds")
