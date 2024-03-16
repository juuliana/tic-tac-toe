from values import empty_position, score
from functions import checkWinner

def getPositions(frame):
    positions = []

    for i in range(3):
        for j in range(3):
            if(frame[i][j] == empty_position):
                positions.append([i, j])

    return positions

def makeMoveIA(frame, player):
    possibilities = getPositions(frame)
    betterMove = None
    betterValue = None
 
    for possibility in possibilities:
        frame[possibility[0]][possibility[1]] = player
        value = minimax(frame, player)
        frame[possibility[0]][possibility[1]] = empty_position

        if(betterValue is None):   
            betterValue = value
            betterMove = possibility
        elif(player == "X"):
            if(value > betterValue):
                betterValue = value
                betterMove = possibility
        elif(player == "O"):
            if(value < betterValue):
                betterValue = value
                betterMove = possibility

    return betterMove[0], betterMove[1]
    
def minimax(frame, player):
    if(player == "X"): player = "O"
    else: player = "X"
    
    possibilities = getPositions(frame)
    betterValue = None

    for possibility in possibilities:
        frame[possibility[0]][possibility[1]] = player
        value = minimax(frame, player)
        frame[possibility[0]][possibility[1]] = empty_position

        if(betterValue is None):   
            betterValue = value
        elif(player == "X"):
            if(value > betterValue):
                betterValue = value
        elif(player == "O"):
            if(value < betterValue):
                betterValue = value

    return betterValue