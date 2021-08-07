import pygame
blackBishop = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackBishop.png')
blackBishop = pygame.transform.scale(blackBishop, (100, 100))

blackKing = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackKing.png')
blackKing = pygame.transform.scale(blackKing, (100, 100))

blackHorse = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackKnight.png')
blackHorse = pygame.transform.scale(blackHorse, (100, 100))

blackPawn = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackPawn.png')
blackPawn = pygame.transform.scale(blackPawn, (100, 100))

blackQueen = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackQueen.png')
blackQueen = pygame.transform.scale(blackQueen, (100, 100))

blackRook = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/blackRook.png')
blackRook = pygame.transform.scale(blackRook, (100, 100))

whiteBishop = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whiteBishop.png')
whiteBishop = pygame.transform.scale(whiteBishop, (100, 100))

whiteKing = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whiteKing.png')
whiteKing = pygame.transform.scale(whiteKing, (100, 100))

whiteHorse = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whiteKnight.png')
whiteHorse = pygame.transform.scale(whiteHorse, (100, 100))

whitePawn = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whitePawn.png')
whitePawn = pygame.transform.scale(whitePawn, (100, 100))

whiteQueen = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whiteQueen.png')
whiteQueen = pygame.transform.scale(whiteQueen, (100, 100))

whiteRook = pygame.image.load('C:/Users/encha_9ba2ozo/PycharmProjects/ChessGame/sexc chess sprites/whiteRook.png')
whiteRook = pygame.transform.scale(whiteRook, (100, 100))

White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (211, 211, 211)
play = pygame.display.set_mode(size=(1000, 800))

def drawBoard(Board):
    for i in range(8):
        for j in range(8):
            if i % 2 == 1:
                if j % 2 == 0:
                    pygame.draw.rect(play, Grey, [j * 100, i * 100, 100, 100], 0)
                else:
                    pygame.draw.rect(play, White, [j * 100, i * 100, 100, 100], 0)
            else:
                if j % 2 == 1:
                    pygame.draw.rect(play, Grey, [j * 100, i * 100, 100, 100], 0)
                else:
                    pygame.draw.rect(play, White, [j * 100, i * 100, 100, 100], 0)

    for i in range(len(Board)):
        for j in range(len(Board)):
            if Board[i][j] == 'bR':
                play.blit(blackRook, (j * 100, i * 100))
            if Board[i][j] == 'bP':
                play.blit(blackPawn, (j * 100, i * 100))
            if Board[i][j] == 'bH':
                play.blit(blackHorse, (j * 100, i * 100))
            if Board[i][j] == 'bB':
                play.blit(blackBishop, (j * 100, i * 100))
            if Board[i][j] == 'bK':
                play.blit(blackKing, (j * 100, i * 100))
            if Board[i][j] == 'bQ':
                play.blit(blackQueen, (j * 100, i * 100))

            if Board[i][j] == 'wR':
                play.blit(whiteRook, (j * 100, i * 100))
            if Board[i][j] == 'wP':
                play.blit(whitePawn, (j * 100, i * 100))
            if Board[i][j] == 'wH':
                play.blit(whiteHorse, (j * 100, i * 100))
            if Board[i][j] == 'wB':
                play.blit(whiteBishop, (j * 100, i * 100))
            if Board[i][j] == 'wK':
                play.blit(whiteKing, (j * 100, i * 100))
            if Board[i][j] == 'wQ':
                play.blit(whiteQueen, (j * 100, i * 100))