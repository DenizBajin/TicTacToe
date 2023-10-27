from random import choice

def checkwin(board):
    for i in range(3):
        if board[i+1][1] == board[i+1][2] == board[i+1][3] and board[i+1][3] != "_":
            return True
        if board[1][i+1] == board[2][i+1] == board[3][i+1] and board[3][i+1] != "_":
            return True
    if board[1][1] == board[2][2] == board[3][3] and board[3][3] != "_":
        return True
    elif board[3][1] == board[2][2] == board[1][3] and board[1][3] != "_":
        return True
    else:
        return False


def checkwhowon(board):
    for i in range(3):
        if board[i+1][1] == board[i+1][2] == board[i+1][3] and board[i+1][3] != "_":
            return board[i+1][1] + " won the game. "
        if board[1][i+1] == board[2][i+1] == board[3][i+1] and board[3][i+1] != "_":
            return board[1][i+1] + " won the game. "
    if board[1][1] == board[2][2] == board[3][3] and board[3][3] != "_":
        return board[1][1] + " won the game. "
    if board[3][1] == board[2][2] == board[1][3] and board[1][3] != "_":
        return board[2][2] + " won the game. "
    return "Game will keep going."


def checkdraw(board):
    filled = 0
    for line in board[1:]:
        for spot in line[1:]:
            if spot == "O" or spot == "X":
                filled += 1
    if filled == 9:
        return True
    else:
        return False


def insert(coordinates, board, letter):
    row = int(coordinates[0])
    column = int(coordinates[2])
    if board[row][column] == "_":
        board[row][column] = letter
    return board


def tictactoe():
    board = [["-","1","2","3"],[1,"_", "_", "_"],[2,"_", "_", "_"],[3,"_", "_", "_"]]
    print("Welcome to TicTacToe. Have fun playing.")
    xo = ["X", "O"]
    turn = choice(xo)
    print(turn + " will make the first move.")
    for item in board:
        print(str(item))
    print("The rows and columns are numbered from 1 to 3 from top to bottom and left to right. ")
    coordinates = input("Type the number of the row and column in the form of row,column with no spaces where you want to place an " + turn + ".")
    if len(coordinates) != 3:
        coordinates = input("Please enter two numbers: one for row and one for column.")
    elif coordinates[0] not in ["1","2","3"] or coordinates[2] not in ["1","2","3"]:
        coordinates = input("The coordinates are either 1, 2, or 3. Please enter valid coordinates.  ")
    elif not(1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[2]) <= 3):
        coordinates = input("Please enter values within the 1-3 range.")
    elif board[int(coordinates[0])][int(coordinates[2])] != "_":
        coordinates = input("The spot is already taken. Enter different coordinates.")
    board = insert(coordinates, board, turn)

    while not checkdraw(board) and not checkwin(board):

        if turn == "X":
            for item in board:
                print(str(item))
            coordinates = input("It is O's turn. Please enter the coordinates of your move.")
            if len(coordinates) != 3:
                coordinates = input("Please enter two numbers: one for row and one for column.")
            elif coordinates[0] not in ["1","2","3"] or coordinates[2] not in ["1","2","3"]:
                coordinates = input("The coordinates are either 1, 2, or 3. Please enter valid coordinates.  ")
            elif not(1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[2]) <= 3):
                coordinates = input("Please enter values within the 1-3 range.")
            elif board[int(coordinates[0])][int(coordinates[2])] != "_":
                coordinates = input("The spot is already taken. Enter different coordinates.")
        board = insert(coordinates, board, "O")
        turn = "O"

        if turn == "O":
            for item in board:
                print(str(item))

            coordinates = input("It is X's turn. Please enter the coordinates of your move.")
            if len(coordinates) != 3:
                coordinates = input("Please enter two numbers: one for row and one for column.")
            elif coordinates[0] not in ["1","2","3"] or coordinates[2] not in ["1","2","3"]:
                coordinates = input("The coordinates are either 1, 2, or 3. Please enter valid coordinates.  ")
            elif not(1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[2]) <= 3):
                coordinates = input("Please enter values within the 1-3 range.")
            elif board[int(coordinates[0])][int(coordinates[2])] != "_":
                coordinates = input("The spot is already taken. Enter different coordinates.")
        board = insert(coordinates, board, "X")
        turn = "X"


    if checkdraw(board):
        return "It is a draw between X and O. Thanks for playing TicTacToe."
    elif checkwin(board):
        return checkwhowon(board)
