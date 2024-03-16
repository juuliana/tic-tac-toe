import pygame 
pygame.font.init()

from values import size, dimension, font_size, white, black, purple
from minimax import makeMoveIA
from functions import createFrame, isValidMove, makeMove, checkWinner

def draw(window, frame):
    for i in range(1, 3):
        pygame.draw.line(window, purple, (0, i * size), (dimension, i * size), 3)
        pygame.draw.line(window, purple, (i * size, 0), (i * size, dimension), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("verdana", font_size)
            x = j * size
            y = i * size

            text = font.render(frame[i][j], 1, white)
            window.blit(text, ((x + 45), (y + 30)))
        
def redraw(window, frame):
    window.fill(black)
    draw(window, frame)

def play():
    window = pygame.display.set_mode((dimension, dimension))
    pygame.display.set_caption("Jogo da Velha")

    frame = createFrame()
    redraw(window, frame)
    pygame.display.update()

    player = "X" # player "O"
    winner = checkWinner(frame)

    while(not winner):
        if(player == "X"):
            played = False

            while(not played):
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    elif(event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/size)
                        j = int(pos[0]/size)
                        played = True
        else:
            i,j = makeMoveIA(frame, player)

        isValid = isValidMove(frame, i, j)

        if(isValid):
            makeMove(frame, i, j, player)

            if(player == "X"): player = "O"
            else: player = "X"

        winner = checkWinner(frame)
        redraw(window, frame)
        pygame.display.update()

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return

play()