import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Constants
EMPTY = ' '  # Define the empty symbol for the board

# Minimax algorithm to decide the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, player_symbol):
        return -1  # Player loses
    if check_winner(board, ai_symbol):
        return 1  # AI wins
    if is_board_full(board):
        return 0  # Tie

    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = ai_symbol
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = player_symbol
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# AI Move function
def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = ai_symbol
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val

    return move

# Check if the current player has won
def check_winner(board, symbol):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == symbol for j in range(3)]) or all([board[j][i] == symbol for j in range(3)]):
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

# Check if the board is full (tie condition)
def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Create the game board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Function to handle the player's move
def player_move(row, col):
    global game_over  # Declare the global variable before modifying it
    if board[row][col] == EMPTY and not game_over:
        board[row][col] = player_symbol
        buttons[row][col].config(text=player_symbol, state="disabled")
        if check_winner(board, player_symbol):
            messagebox.showinfo("Game Over", f"Player {player_symbol} wins!")
            game_over = True
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True
        else:
            ai_move()

# Function to handle the AI's move
def ai_move():
    global game_over  # Declare the global variable before modifying it
    if game_over:
        return
    move = best_move(board)
    row, col = move
    board[row][col] = ai_symbol
    buttons[row][col].config(text=ai_symbol, state="disabled")
    if check_winner(board, ai_symbol):
        messagebox.showinfo("Game Over", f"AI {ai_symbol} wins!")
        game_over = True
    elif is_board_full(board):
        messagebox.showinfo("Game Over", "It's a tie!")
        game_over = True

# Function to start a new game
def new_game():
    global game_over  # Declare the global variable before modifying it
    global player_symbol, ai_symbol
    game_over = False

    # Ask the user to select X or O
    player_symbol = simpledialog.askstring("Player Choice", "Do you want to play as X or O?").upper()

    if player_symbol not in ['X', 'O']:
        # If the user input is invalid, show a message and return without starting the game
        messagebox.showwarning("Invalid Choice", "Please choose either X or O.")
        return

    # Set AI symbol based on player's choice
    ai_symbol = 'X' if player_symbol == 'O' else 'O'

    # Reset the board
    for row in range(3):
        for col in range(3):
            board[row][col] = EMPTY
            buttons[row][col].config(text=EMPTY, state="normal")

# UI setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Global variables
board = create_board()
buttons = [[None for _ in range(3)] for _ in range(3)]
game_over = False
player_symbol = None
ai_symbol = None

# Create buttons for the Tic Tac Toe grid
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=EMPTY, font=('normal', 40), width=5, height=2,
                                      command=lambda r=row, c=col: player_move(r, c))
        buttons[row][col].grid(row=row, column=col)

# Add a new game button
new_game_button = tk.Button(root, text="New Game", font=('normal', 15), width=20, command=new_game)
new_game_button.grid(row=3, column=0, columnspan=3)

# Run the game loop
new_game()  # Ask the user to select X or O at the start
root.mainloop()
