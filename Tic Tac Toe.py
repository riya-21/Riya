# these lines are to start the random choices that the computer will be entering as well as set the initial board
from random import choice
initial_board = {"A":" ", "B":" ","C":" ","D":" ","E":" ","F":" ","G":" ","H":" ","I":" "}
my_board = {}

# this is the game board that the player uses as reference to play
def game_board():
    print("   A    |   B    |   C    ")
    print("--------+--------+--------")
    print("   D    |   E    |   F    ")
    print("--------+--------+--------")
    print("   G    |   H    |   I    ")

# this is the game board the player plays on
def draw_current_board(current_board):
    print("   "+current_board["A"] +"    |   "+current_board["B"] +"    |   "+current_board["C"] +"    ")
    print("--------+--------+--------")
    print("   " + current_board["D"] + "    |   " + current_board["E"] + "    |   " + current_board["F"] + "    ")
    print("--------+--------+--------")
    print("   " + current_board["G"] + "    |   " + current_board["H"] + "    |   " + current_board["I"] + "    ")


# this records the move of the player
def player_move(mark):
    if mark == "X":  # this is a user move
        response = input("In which position would you like to place your mark?").strip().title()
    else:
        response = get_system_move()
    my_board[response] = mark

# this is how I got the computer's move through a random generated choice
def get_system_move ():
    position = choice(list(my_board.keys()))
    while my_board[position] != " ":
        position = choice(list(my_board.keys()))
    return position

# this is how I told the program that three in a row is a victory
def victory():
    victory = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["A", "D", "G"],["B", "E", "H"],["C", "F", "I"],
               ["C", "E", "G"],["A", "E", "I"]]
    winner = "None"
    for combination in victory:
        if my_board[combination[0]] != " " and my_board[combination[0]] == my_board[combination[1]]  and my_board[combination[0]] == my_board[combination[2]]:
            winner = my_board[combination[0]]
            break
    return winner

# this is how I told the program that if the board is filled with no victory, it is a draw
def draw():
    if victory() == "None" and  " " not in my_board.values():
        return True
    else:
        return False

# this is the main program
rerun = "Y"
print("Welcome to online tic tac toe!\n")
while rerun == "Y": # this re-runs the tic tac toe if user chooses to
    game_board()
    print("\n")
    print("You will be playing as X and the computer will play as O\n")
    my_board = initial_board.copy()
    while  victory() == "None" and not draw(): # this is how the game keeps playing until a victory or draw
        player_move("X")
        if victory() != "None":
            draw_current_board(my_board)
            break
        if not draw():
            player_move("O")
        draw_current_board(my_board)

    winner = victory()
    if winner != "None": # this is how I checked for a victory
        if winner == "X":
            rerun = input("Congratulations! You won!!! Enter Y to play again. Press any other key to quit.").strip().title()
        else:
            rerun = input("Sorry, you lost :(  Enter Y to play again. Press any other key to quit.").strip().title()
    else:
        rerun = input("This game was a draw. Enter Y to play again. Press any other key to quit.").strip().title()




