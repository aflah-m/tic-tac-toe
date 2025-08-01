import random

current_player = "X"
winner = ""
tie = False
game_running = True


#making board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("__________")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("__________")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("__________")

#Takin player input
def player_input(board, current_player):
    inp_list = ["1","2","3","4","5","6","7","8","9"]
    print("Player's turn!!!")

    valid = False
    while not valid:
        inp = (input("Enter a number [1-9]"))
        if inp in inp_list:
            inp = int(inp)
            if board[inp - 1] != "-":
                print("Place is reserved")
            else:
                valid = True
        else:
            print("Not Valid")
    board[inp - 1] = current_player

#Checking win & tie
def check_game_state(board,current_player):
    global winner
    global tie
    
    #Row
    if (
    board[0] == board[1] == board[2] != "-" or
    board[3] == board[4] == board[5] != "-" or
    board[6] == board[7] == board[8] != "-" or
    board[0] == board[3] == board[6] != "-" or
    board[1] == board[4] == board[7] != "-" or
    board[2] == board[5] == board[8] != "-" or
    board[0] == board[4] == board[8] != "-" or
    board[6] == board[4] == board[2] != "-"
):       
        winner = current_player
    
    #Checkin tie
    if "-" not in board:
        tie = True

#Switching player
def switch_player():
        global current_player
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X" 

#End game if a winner is decided or in case of tie
def end_game(winner, tie):
    global game_running
    if winner != "" or tie == True:
        print_board(board)
        game_running = False

#Computer AI
def computer_ai(board, current_player):
    comp_choice = -1
    for i in range(0,9):
        if board[i] == "-":
            board[i] = "O"
            
            #Row
            if (board[0] == board[1] == board[2] == "O" or
                board[3] == board[4] == board[5] == "O" or
                board[6] == board[7] == board[8] == "O" or
                board[0] == board[3] == board[6] == "O" or
                board[1] == board[4] == board[7] == "O" or
                board[2] == board[5] == board[8] == "O" or
                board[0] == board[4] == board[8] == "O" or
                board[6] == board[4] == board[2] == "O"):
                comp_choice = i
                break
            board[i] = "-"
    
    if comp_choice == -1:
        comp_choice = random.randint(0, 8)
        while(board[comp_choice] != "-"):
            comp_choice = random.randint(0, 8)
        board[comp_choice] = current_player
                          
#playing the game
while game_running:
    print_board(board)
    player_input(board, current_player)
    check_game_state(board, current_player)     
    end_game(winner, tie)
    if not game_running:
        break
    switch_player()
    computer_ai(board, current_player)
    check_game_state(board, current_player)     
    end_game(winner, tie)
    if not game_running:
        break
    switch_player()

print("")
if winner == "X":
    print("!!! Player has Won !!!")
elif winner == "O":
    print("!!! Computer Has Won !!!")
elif tie:
    print("!!! The game is draw !!!")
print("")
print("!!! END !!!")
