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


#Switch player


#Check for Win or Tie again
while gameRunning:
    printGameboard(board)
    playerInput(board)
    