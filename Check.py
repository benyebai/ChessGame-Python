import copy as c
def movePieceBlackCheck(startFinish, Board, haveMoved):
    kill = ('wR', 'wH', 'wB', 'wQ', 'wK', 'wP')
    def blackPawn():
        row = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]
        # double move
        if startFinish[0] in row:
            if startFinish[0][0] == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] + 2:
                return True
        # normally
        if startFinish[0][0] == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] + 1:
            if Board[startFinish[1][1]][startFinish[1][0]] == '  ':
                return True
        # kill left
        if startFinish[0][0] + 1 == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] + 1:
            if Board[startFinish[1][1]][startFinish[1][0]] in kill:
                return True
        # kill right
        if startFinish[0][0] - 1 == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] + 1:
            if Board[startFinish[1][1]][startFinish[1][0]] in kill:
                return True

    def blackHorse():
        if ((abs(startFinish[0][0] - startFinish[1][0]) ** 2) + (abs(startFinish[0][1] - startFinish[1][1]) ** 2)) ** .5 == 5 ** .5 and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def blackBishop():
        def bishopCheck():
            work = True
            # up-right
            if startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] - i] != '  ':
                        work = False

            # up-left
            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] + i] != '  ':
                        work = False

            # bottom-right
            elif startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] - i] != '  ':
                        work = False

            # bottom-left
            else:  # startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] + i] != '  ':
                        work = False

            if work:
                return True
            else:
                return False

        if bishopCheck() and abs(startFinish[0][0] - startFinish[1][0]) == abs(startFinish[0][1] - startFinish[1][1]) and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def blackRook():
        def rookCheck():
            work = True

            # moving-up
            if startFinish[0][0] == startFinish[1][0] and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, startFinish[0][1] - startFinish[1][1]):
                    if Board[startFinish[1][1] + i][startFinish[1][0]] != '  ':
                        work = False

            # moving-down
            elif startFinish[0][0] == startFinish[1][0] and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][1] - startFinish[1][1])):
                    if Board[startFinish[1][1] - i][startFinish[1][0]] != '  ':
                        work = False

            # moving-left
            elif startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] > 0:
                for i in range(1, startFinish[0][0] - startFinish[1][0]):
                    if Board[startFinish[1][1]][startFinish[1][0] + i] != '  ':
                        work = False

            # moving-right
            else:  # startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1]][startFinish[1][0] - i] != '  ':
                        work = False
            if work:
                return True
            else:
                return False

        if (startFinish[0][0] == startFinish[1][0] or startFinish[0][1] == startFinish[1][1]) and rookCheck() and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            if 'bR' not in haveMoved:
                haveMoved.append('bR')
            return True

    def blackQueen():
        def queenCheck():
            work = True

            if startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] - i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] + i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] - i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] + i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] == 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, startFinish[0][1] - startFinish[1][1]):
                    if Board[startFinish[1][1] + i][startFinish[1][0]] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] == 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][1] - startFinish[1][1])):
                    if Board[startFinish[1][1] - i][startFinish[1][0]] != '  ':
                        work = False

            elif startFinish[0][1] - startFinish[1][1] == 0 and startFinish[0][0] - startFinish[1][0] > 0:
                for i in range(1, startFinish[0][0] - startFinish[1][0]):
                    if Board[startFinish[1][1]][startFinish[1][0] + i] != '  ':
                        work = False

            else:  # startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1]][startFinish[1][0] - i] != '  ':
                        work = False

            if work:
                return True
            else:
                return False

        if startFinish[0][0] == startFinish[1][0] or startFinish[0][1] == startFinish[1][1]:
            horizontal = True
        else:
            horizontal = False

        if abs(startFinish[0][0] - startFinish[1][0]) == abs(startFinish[0][1] - startFinish[1][1]):
            diagonal = True
        else:
            diagonal = False

        if queenCheck() and (horizontal or diagonal) and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def blackKing():
        if Board[startFinish[1][1]][startFinish[1][0]] == 'bR' and 'bK' not in haveMoved and 'bR' not in haveMoved and startFinish[1][0] == 7:
            return 'Castle Right'
        if Board[startFinish[1][1]][startFinish[1][0]] == 'bR' and 'bK' not in haveMoved and 'bR' not in haveMoved and startFinish[1][0] == 0:
            return 'Castle Left'
        if -1 <= startFinish[0][0] - startFinish[1][0] <= 1 and -1 <= startFinish[0][1] - startFinish[1][1] <= 1 and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            if 'bK' not in haveMoved:
                haveMoved.append('bK')
            return 'Success'

    pieceChosen = Board[startFinish[0][1]][startFinish[0][0]]

    if pieceChosen == 'bP':
        if blackPawn():
            if startFinish[1][1] == 7:
                Board[startFinish[1][1]][startFinish[1][0]] = 'bQ'
                Board[startFinish[0][1]][startFinish[0][0]] = '  '
            else:
                Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
                Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'bH':
        if blackHorse():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'bB':
        if blackBishop():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'bR':
        if blackRook():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'bQ':
        if blackQueen():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'bK':
        if blackKing() == 'Success':
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True

        elif blackKing() == 'Castle Right':
            Board[0][6] = pieceChosen
            Board[0][5] = 'bR'
            Board[startFinish[1][1]][startFinish[1][0]] = '  '
            Board[startFinish[0][1]][startFinish[0][0]] = '  '

        elif blackKing() == 'Castle Left':
            Board[0][1] = pieceChosen
            Board[0][2] = 'bR'
            Board[startFinish[1][1]][startFinish[1][0]] = '  '
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
        else:
            return False

def movePieceWhiteCheck(startFinish, Board, haveMoved):
    kill = ('bR', 'bH', 'bB', 'bQ', 'bK', 'bP')
    def whitePawn():
        row = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]]

        # double move
        if startFinish[0] in row:
            if startFinish[0][0] == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] - 2:
                return True
        # normally
        if startFinish[0][0] == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] - 1:
            if Board[startFinish[1][1]][startFinish[1][0]] == '  ':
                return True
        # kill left
        if startFinish[0][0] - 1 == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] - 1:
            if Board[startFinish[1][1]][startFinish[1][0]] in kill:
                return True
        # kill right
        if startFinish[0][0] + 1 == startFinish[1][0] and startFinish[1][1] == startFinish[0][1] - 1:
            if Board[startFinish[1][1]][startFinish[1][0]] in kill:
                return True

    def whiteHorse():
        if ((abs(startFinish[0][0] - startFinish[1][0]) ** 2) + (abs(startFinish[0][1] - startFinish[1][1]) ** 2)) ** .5 == 5 ** .5 and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def whiteBishop():
        def bishopCheck():
            work = True
            # up-right
            if startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] - i] != '  ':
                        work = False

            # up-left
            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] + i] != '  ':
                        work = False

            # bottom-right
            elif startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] - i] != '  ':
                        work = False

            # bottom-left
            else:  # startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] + i] != '  ':
                        work = False

            if work:
                return True
            else:
                return False

        if bishopCheck() and abs(startFinish[0][0] - startFinish[1][0]) == abs(startFinish[0][1] - startFinish[1][1]) and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def whiteRook():
        def rookCheck():
            work = True

            # moving-up
            if startFinish[0][0] == startFinish[1][0] and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, startFinish[0][1] - startFinish[1][1]):
                    if Board[startFinish[1][1] + i][startFinish[1][0]] != '  ':
                        work = False

            # moving-down
            elif startFinish[0][0] == startFinish[1][0] and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][1] - startFinish[1][1])):
                    if Board[startFinish[1][1] - i][startFinish[1][0]] != '  ':
                        work = False

            # moving-left
            elif startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] > 0:
                for i in range(1, startFinish[0][0] - startFinish[1][0]):
                    if Board[startFinish[1][1]][startFinish[1][0] + i] != '  ':
                        work = False

            # moving-right
            else:  # startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1]][startFinish[1][0] - i] != '  ':
                        work = False
            if work:
                return True
            else:
                return False

        if (startFinish[0][0] == startFinish[1][0] or startFinish[0][1] == startFinish[1][1]) and rookCheck() and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            if 'wR' not in haveMoved:
                haveMoved.append('wR')
            return True

    def whiteQueen():
        def queenCheck():
            work = True

            if startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] - i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] + i][startFinish[1][0] + i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] < 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] - i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] > 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1] - i][startFinish[1][0] + i] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] == 0 and startFinish[0][1] - startFinish[1][1] > 0:
                for i in range(1, startFinish[0][1] - startFinish[1][1]):
                    if Board[startFinish[1][1] + i][startFinish[1][0]] != '  ':
                        work = False

            elif startFinish[0][0] - startFinish[1][0] == 0 and startFinish[0][1] - startFinish[1][1] < 0:
                for i in range(1, abs(startFinish[0][1] - startFinish[1][1])):
                    if Board[startFinish[1][1] - i][startFinish[1][0]] != '  ':
                        work = False

            elif startFinish[0][1] - startFinish[1][1] == 0 and startFinish[0][0] - startFinish[1][0] > 0:
                for i in range(1, startFinish[0][0] - startFinish[1][0]):
                    if Board[startFinish[1][1]][startFinish[1][0] + i] != '  ':
                        work = False

            else:  # startFinish[0][1] == startFinish[1][1] and startFinish[0][0] - startFinish[1][0] < 0:
                for i in range(1, abs(startFinish[0][0] - startFinish[1][0])):
                    if Board[startFinish[1][1]][startFinish[1][0] - i] != '  ':
                        work = False

            if work:
                return True
            else:
                return False

        if startFinish[0][0] == startFinish[1][0] or startFinish[0][1] == startFinish[1][1]:
            horizontal = True
        else:
            horizontal = False

        if abs(startFinish[0][0] - startFinish[1][0]) == abs(startFinish[0][1] - startFinish[1][1]):
            diagonal = True
        else:
            diagonal = False

        if queenCheck() and (horizontal or diagonal) and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            return True

    def whiteKing():
        if Board[startFinish[1][1]][startFinish[1][0]] == 'wR' and 'wK' not in haveMoved and 'wR' not in haveMoved and startFinish[1][0] == 7:
            return 'Castle Right'
        if Board[startFinish[1][1]][startFinish[1][0]] == 'wR' and 'wK' not in haveMoved and 'wR' not in haveMoved and startFinish[1][0] == 0:
            return 'Castle Left'
        if -1 <= startFinish[0][0] - startFinish[1][0] <= 1 and -1 <= startFinish[0][1] - startFinish[1][1] <= 1 and (Board[startFinish[1][1]][startFinish[1][0]] in kill or Board[startFinish[1][1]][startFinish[1][0]] == '  '):
            if 'wK' not in haveMoved:
                haveMoved.append('wK')
            return 'Success'


    pieceChosen = Board[startFinish[0][1]][startFinish[0][0]]

    if pieceChosen == 'wP':
        if whitePawn():
            if startFinish[1][1] == 0:
                Board[startFinish[1][1]][startFinish[1][0]] = 'wQ'
                Board[startFinish[0][1]][startFinish[0][0]] = '  '
            else:
                Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
                Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'wH':
        if whiteHorse():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False


    if pieceChosen == 'wB':
        if whiteBishop():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'wR':
        if whiteRook():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'wQ':
        if whiteQueen():
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True
        else:
            return False

    if pieceChosen == 'wK':
        if whiteKing() == 'Success':
            Board[startFinish[1][1]][startFinish[1][0]] = pieceChosen
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
            return True

        elif whiteKing() == 'Castle Right':
            Board[7][6] = pieceChosen
            Board[7][5] = 'wR'
            Board[startFinish[1][1]][startFinish[1][0]] = '  '
            Board[startFinish[0][1]][startFinish[0][0]] = '  '

        elif whiteKing() == 'Castle Left':
            Board[7][1] = pieceChosen
            Board[7][2] = 'wR'
            Board[startFinish[1][1]][startFinish[1][0]] = '  '
            Board[startFinish[0][1]][startFinish[0][0]] = '  '
        else:
            return False

def whiteCheck(Board, haveMoved, startFinish):
    copy = c.deepcopy(Board)
    movePieceWhiteCheck(startFinish, copy, haveMoved)


    whiteKingPos = []
    for i in range(8):
        for j in range(8):
            if copy[i][j] == 'wK':
                whiteKingPos.append(j)
                whiteKingPos.append(i)

    for i in range(8):
        for j in range(8):
            checkPos = []
            temp = []
            if copy[i][j][0] == 'b':
                temp.append(j)
                temp.append(i)
                checkPos.append(temp)
                checkPos.append(whiteKingPos)
                if movePieceBlackCheck(checkPos, copy, haveMoved):
                    return True
    return False

def blackCheck(Board, haveMoved, startFinish):
    copy = c.deepcopy(Board)
    movePieceBlackCheck(startFinish, copy, haveMoved)


    blackKingPos = []
    for i in range(8):
        for j in range(8):
            if copy[i][j] == 'bK':
                blackKingPos.append(j)
                blackKingPos.append(i)

    for i in range(8):
        for j in range(8):
            checkPos = []
            temp = []
            if copy[i][j][0] == 'w':
                temp.append(j)
                temp.append(i)
                checkPos.append(temp)
                checkPos.append(blackKingPos)
                if movePieceWhiteCheck(checkPos, copy, haveMoved):
                    return True
    return False

