import pygame
import Move
import sys
import DrawBoard
import Check

pygame.init()

play = pygame.display.set_mode(size=(1000, 800))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Times New Roman, Arial', 25, False, False)

# colours pog
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (211, 211, 211)


Board = [['bR', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bR'],
         ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
         ['wR', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wR']]

haveMoved = []

def checkWinner():
    wK = False
    bK = False
    for i in range(len(Board)):
        for j in range(len(Board)):
            if Board[i][j] == 'wK':
                wK = True
            if Board[i][j] == 'bK':
                bK = True
    if wK and bK:
        return
    if wK and not bK:
        return "white win"
    if bK and not wK:
        return "black win"


startFinish = []
running = True

TURN = 'WHITE'


def checkPointsWhite():
    bishop = 2
    horse = 2
    pawn = 8
    rook = 2
    queen = 1

    for j in range(8):
        bishop -= Board[j].count('bB')
        horse -= Board[j].count('bH')
        pawn -= Board[j].count('bP')
        rook -= Board[j].count('bR')
        queen -= Board[j].count('bQ')

    whitePoints = (bishop * 3) + (horse * 3) + pawn + (rook * 5) + (max(queen, 0) * 9)
    return whitePoints

def checkPointsBlack():
    bishop = 2
    horse = 2
    pawn = 8
    rook = 2
    queen = 1

    for j in range(8):
        bishop -= Board[j].count('wB')
        horse -= Board[j].count('wH')
        pawn -= Board[j].count('wP')
        rook -= Board[j].count('wR')
        queen -= Board[j].count('wQ')

    blackPoints = (bishop * 3) + (horse * 3) + pawn + (rook * 5) + (max(queen, 0) * 9)
    return blackPoints


wTimer = 300

bTimer = 300
dt = 0
while running:
    play.fill(Black)
    DrawBoard.drawBoard(Board)

    whoWin = ''
    # points display
    bPointsDisplay = font.render('points : ' + str(checkPointsBlack()), True, White)
    play.blit(bPointsDisplay, [850, 80])

    wPointsDisplay = font.render('points : ' + str(checkPointsWhite()), True, White)
    play.blit(wPointsDisplay, [850, 680])

    # timer
    wTimerDis = str(int(wTimer / 60)) + ':' + str(wTimer % 60)[0:2]
    wCountdown = font.render(str(wTimerDis), True, White)
    play.blit(wCountdown, [830, 750])

    bTimerDis = str(int(bTimer / 60)) + ':' + str(bTimer % 60)[0:2]
    bCountdown = font.render(str(bTimerDis), True, White)
    play.blit(bCountdown, [830, 10])


    if TURN == 'WHITE':
        wTimer -= dt
        if wTimer <= 0:
            print('BLACK WIN')
            break
    else:
        bTimer -= dt
        if wTimer <= 0:
            print('WHITE WIN')
            break




    for event in pygame.event.get():
        # using space to quit out of the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

        # getting the location of the click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                posofClick = pygame.mouse.get_pos()
                startFinish.append(list((posofClick[0] // 100, posofClick[1] // 100)))

        # holds start and end point
        if len(startFinish) > 0:
            if Board[startFinish[0][1]][startFinish[0][0]] == '  ':
                startFinish = []

        if len(startFinish) == 2:
            if startFinish[0] != startFinish[1]:

                # who's Turn ---------------------------
                if TURN == 'WHITE':

                    if Move.movePieceWhite(startFinish, Board, haveMoved):
                        if checkWinner() == 'white win':
                            whoWin = 'WHITE WIN'
                            break
                        startFinish = []
                        wTimer += 2
                        TURN = 'BLACK'
                    else:
                        print("White's Turn")
                        startFinish = []

                elif TURN == 'BLACK':

                    if Move.movePieceBlack(startFinish, Board, haveMoved):
                        if checkWinner() == 'black win':
                            whoWin = 'BLACK WIN'
                            break
                        startFinish = []
                        TURN = 'WHITE'
                        bTimer += 2
                    else:
                        print("Black's Turn")
                        startFinish = []
                # ---------------------------------------

            else:
                print('invalid move')
                startFinish = []
    if whoWin != '':
        print(whoWin)
        break
    dt = clock.tick(30) / 1000
    pygame.display.flip()
