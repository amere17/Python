# ------- TIC-TAC-TOE game -------

# ______________________________________
# Board of the game and Global Variables
GameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-", ]

game_going = True
winner = None
curr_player = "X"


# ______________________________________

# _____________ Functions ______________
def reset_data():
    global game_going, winner, curr_player, GameBoard
    game_going = True
    winner = None
    curr_player = "X"
    for i in range(len(GameBoard)):
        GameBoard[i] = "-"



# Display the Board
def display_game():
    print(GameBoard[0] + "|" + GameBoard[1] + "|" + GameBoard[2])
    print(GameBoard[3] + "|" + GameBoard[4] + "|" + GameBoard[5])
    print(GameBoard[6] + "|" + GameBoard[7] + "|" + GameBoard[8])


# Start New Game
def new_game():
    display_game()

    while game_going:
        handle_turn(curr_player)
        check_if_game_over()
        switch_player()

    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner is None:
        print("Tie.")
    
    # Play again method
    if input("Play Again?: y/n ") == "y":
        reset_data()
        new_game()
    else:
        return


# Turns between players
def handle_turn(player):
    print(player + "'s turn.")
    pos = int(input("Choose a position from 1-9: "))

    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        pos = int(input("Invalid input. Choose a position from 1-9: "))

    while GameBoard[pos - 1] != "-":
        pos = int(input("Try Again. Choose a position from 1-9: "))

    pos = pos - 1
    GameBoard[pos] = player
    display_game()

# check if the gam has ended
def check_if_game_over():
    check_if_win()
    check_if_tie()

# check if there is a winner
def check_if_win():
    global winner
    # rows,columns,diagonals
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_going
    # check rows of the game if there is a winner
    row1 = GameBoard[0] == GameBoard[1] == GameBoard[2] != "-"
    row2 = GameBoard[3] == GameBoard[4] == GameBoard[5] != "-"
    row3 = GameBoard[6] == GameBoard[7] == GameBoard[8] != "-"

    if row1 or row2 or row3:
        game_going = False
    if row1:
        return GameBoard[0]
    elif row2:
        return GameBoard[3]
    elif row3:
        return GameBoard[6]
    return


def check_columns():
    global game_going
    # check columns of the game if there is a winner
    col1 = GameBoard[0] == GameBoard[3] == GameBoard[6] != "-"
    col2 = GameBoard[1] == GameBoard[4] == GameBoard[7] != "-"
    col3 = GameBoard[2] == GameBoard[5] == GameBoard[8] != "-"

    if col1 or col2 or col3:
        game_going = False
    if col1:
        return GameBoard[0]
    elif col2:
        return GameBoard[1]
    elif col3:
        return GameBoard[2]
    return


def check_diagonals():
    global game_going
    # check diagonals of the game if there is a winner
    diag1 = GameBoard[0] == GameBoard[4] == GameBoard[8] != "-"
    diag2 = GameBoard[6] == GameBoard[4] == GameBoard[2] != "-"

    if diag1 or diag2:
        game_going = False
    if diag1:
        return GameBoard[0]
    elif diag2:
        return GameBoard[2]
    return
# ______________________________________

def check_if_tie():
    global game_going
    if "-" not in GameBoard:
        game_going = False
    return

def switch_player():
    global curr_player

    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"

    return


new_game()
