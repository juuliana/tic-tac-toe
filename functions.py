from values import empty_position

#frame ----------------------------------
def createFrame():
    return [
        [empty_position, empty_position, empty_position],
        [empty_position, empty_position, empty_position],
        [empty_position, empty_position, empty_position],
    ]
#----------------------------------------

#move -----------------------------------
def isValidMove(frame, i, j):
    return frame[i][j] == empty_position

def makeMove(frame, i, j, player):
    frame[i][j] = player
#----------------------------------------

#winner ---------------------------------
def checkWinner(frame):
    #lines
    for i in range(3):
        completeLines = frame[i][0] == frame[i][1] == frame[i][2]
        if(completeLines and frame[i][0] != empty_position):
            return frame[i][0]
    
    #columns
    for j in range(3):
        completeColumns = frame[0][j] == frame[1][j] == frame[2][j]
        if(completeColumns and frame[0][j] != empty_position):
            return frame[0][j]

    #diagonals
    completeFirstDiagonal = frame[0][0] == frame[1][1] == frame[2][2]
    completeSecondDiagonal = frame[0][2] == frame[1][1] == frame[2][0]

    if(completeFirstDiagonal and frame[0][0] != empty_position):
        return frame[0][0]
    
    if(completeSecondDiagonal and frame[0][2] != empty_position):
        return frame[0][2]
    
    for i in range(3):
        for j in range(3):
            if(frame[i][j] == empty_position):
                return False
            
    return "EMPATE"
#----------------------------------------
    