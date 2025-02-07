# Tic_Tac_Toe in python 
Here's a simple explanation of the code step by step:

**1. Imports:**
tkinter: A Python library to create graphical user interfaces (GUIs). We're using it to make the Tic Tac Toe board and buttons.
messagebox: A module of tkinter to show pop-up message boxes (like for game results).
simpledialog: Another tkinter module that lets us ask the user for simple inputs (like choosing X or O).

**2. Constants:**
EMPTY = ' ': This represents an empty space on the Tic Tac Toe board. We'll use it to initialize the board cells.

**3. Minimax Algorithm (used by AI to play):**
The Minimax algorithm is a decision-making algorithm used for game theory. The AI uses it to decide its best move.
**minimax(board, depth, is_maximizing):**
This function is called recursively. It calculates the "best" move for the AI and player by looking ahead at possible moves.
is_maximizing tells whether the AI or the player is making the move.
If it's the AI's turn (is_maximizing=True), it tries to maximize the AI's score.
If it's the player's turn (is_maximizing=False), it tries to minimize the AI's score (because the player tries to win and block the AI).
The function checks the winner, board state (if full or not), and recursively explores possible game states.
**best_move(board):**
This function uses the minimax() algorithm to calculate and return the best move for the AI by evaluating all possible moves.

**4. Game Logic Functions:**
check_winner(board, symbol): This function checks if a given symbol (either player or AI) has won the game. It looks at rows, columns, and diagonals to see if all three positions have the same symbol.
**is_board_full(board):** This function checks if the board is completely filled. If there are any empty spaces (EMPTY), it returns False, otherwise True. 

**5. Board Setup and Functions:**
**create_board()**: This function creates a 3x3 board for the Tic Tac Toe game, where each cell is initialized to EMPTY (an empty space).
**player_move(row, col):** This function handles the player's move. If the selected cell is empty and the game isn't over, the player's symbol is placed in the cell. It then checks if the player won, if the board is full (tie), or it’s the AI’s turn.
**ai_move():** This function calculates and makes the AI's move using the best_move() function. After the AI moves, it checks if the AI has won or if it's a tie.

**6. New Game Setup:**
**new_game():** This function starts a new game:
It asks the user to choose whether they want to play as X or O using a pop-up dialog.
If the user enters a valid choice, it sets the AI's symbol to the opposite one (so if the player chooses X, the AI gets O and vice versa).
It resets the board and prepares it for a new game.

**7. User Interface (UI):**
**root = tk.Tk():** This creates the main window for the game.
**buttons[][]:** This is a 3x3 grid of buttons that represent each cell in the Tic Tac Toe board. We use tk.Button() to create each button and place it in a grid.
**new_game_button:** A button labeled "New Game" that starts a new game when clicked.

**8. Game Loop:**
new_game() is called when the program starts, which will prompt the user to select X or O.
**root.mainloop():** This starts the event loop, which keeps the window running and listens for user actions (like clicking buttons).

**9. Flow of the Game:**
The player is prompted to choose X or O.
The game starts with the player’s move. When the player clicks a cell, it places the player's symbol in that cell.
After the player’s move, the AI calculates its best move and places its symbol.
The game checks if there's a winner or if it's a tie after every move.
If the game is over (win/tie), a pop-up shows the result.
The player can start a new game by clicking the "New Game" button.
