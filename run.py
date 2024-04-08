import random

#Create board
board = [ "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


#Printing the gameboard
def printGameboard(board):
    print(board[0]+ " | "+ board[1]+ " | "+ board[2])
    print("-----------")
    print(board[3]+ " | "+ board[4]+ " | "+ board[5])
    print("-----------")
    print(board[6]+ " | "+ board[7]+ " | "+ board[8])


#Take player input

def playerInput(board):
    inp = int(input("Enter a number from 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp -1]== "-":
        board[inp -1] = currentPlayer
    else:
        print("The place is already taken or you did't enter a number from 1 to 9!")



#Check for Win or Tie
def checkHorisontal(board):
    global winner
    if board[0] == board[1] == board [3] and board[0] !="-" :
        
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-" :
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board [6] and board[0] !="-" :        
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-" :        
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-" :        
        winner = board[2]
        return True
def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner= board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checkTie(board):
    if "-" not in board:
        global gameRunning
        printGameboard(board)
        print("It's a TIE")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorisontal(board) and checkRow(board) :
        print(f"The winner is {winner}")

#Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer = "X"

#computer


#Check for Win or Tie again
while gameRunning:
    printGameboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
 
    