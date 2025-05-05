import random

PLAYER = 'X'
COMPUTER = 'O'
EMPTY = ' '

def check_winner(board, symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, is_maximizing):
    if check_winner(board, COMPUTER):
        return 10
    if check_winner(board, PLAYER):
        return -10
    if not get_available_moves(board):
        return 0

    best_score = -float('inf') if is_maximizing else float('inf')
    for i, j in get_available_moves(board):
        board[i][j] = COMPUTER if is_maximizing else PLAYER
        score = minimax(board, not is_maximizing)
        board[i][j] = EMPTY
        best_score = max(best_score, score) if is_maximizing else min(best_score, score)

    return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i, j in get_available_moves(board):
        board[i][j] = COMPUTER
        score = minimax(board, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player move
        try:
            row, col = map(int, input("Enter your move (row col) [0-2]: ").split())
            if board[row][col] != EMPTY:
                print("Invalid move, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, enter two numbers between 0 and 2.")
            continue

        board[row][col] = PLAYER
        print_board(board)

        if check_winner(board, PLAYER):
            print("You win!")
            break

        if not get_available_moves(board):
            print("It's a tie!")
            break

        # Computer move
        print("Computer's move:")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = COMPUTER
        print_board(board)

        if check_winner(board, COMPUTER):
            print("Computer wins!")
            break

        if not get_available_moves(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
