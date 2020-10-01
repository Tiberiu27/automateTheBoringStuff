def isValidChessBoard(board):
    charBoardList = ['a','b','c','d','e','f','g','h']
    intBoardList = ['1','2','3','4','5','6','7','8']
    chessBoardList = [] #valid move spaces

    for i in charBoardList: #creating the list for valid move spaces
        for j in intBoardList:
            chessBoardList.append(i+j)

    print(chessBoardList) #test valid move spaces

    chestPieces = [['pawn', 'knight', 'queen', 'king','bishop', 'tower'], ['w','b']]
    for k in range(7):
        chestPieces[0].append(chestPieces[0][0])
    finalChestPieces = []

    for i in chestPieces[0]:
        for j in chestPieces[1]:
            finalChestPieces.append(j+i)



    checkKey, checkValue = list(board.items())[0]


    if  checkKey not in chessBoardList:
        print('not a valid location')
        return False
    else:
        if checkValue not in finalChestPieces:
            print('not a valid piece')
            return False
        print('Nice move! Your ' + checkValue + ' is now at position ' + checkKey)
        return True





move = {'a2': 'bking'}

isValidChessBoard(move)