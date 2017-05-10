theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}


def printBoard (board) :
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def movePos():
    move = input()

    while move not in theBoard.keys():
        print('There is no ['+move+ '] position. You should input correct positon. Try again')
        move = input()

    return move


def checkMoveValid(move):
    if theBoard[move] != ' ':
        print('Already marked! Select another position!!')
        return False
    else:
        return True


def checkWinner(theBoard, turn):
    return ((theBoard['1'] == turn and theBoard['2'] == turn and theBoard['3'] == turn )
    or(theBoard['4'] == turn and theBoard['5'] == turn and theBoard['6'] == turn)
    or(theBoard['7'] == turn and theBoard['8'] == turn and theBoard['9'] == turn)
    or(theBoard['1'] == turn and theBoard['4'] == turn and theBoard['7'] == turn)
    or(theBoard['2'] == turn and theBoard['5'] == turn and theBoard['8'] == turn)
    or(theBoard['3'] == turn and theBoard['6'] == turn and theBoard['9'] == turn)
    or(theBoard['1'] == turn and theBoard['5'] == turn and theBoard['9'] == turn)
    or(theBoard['7'] == turn and theBoard['5'] == turn and theBoard['3'] == turn))


def checkTied(theBoard):
    for v in theBoard.values():
        if v == ' ':
            return False

    return True



def runTicTacToe():
    gameStart = True
    turn = 'O'

    print('=== Position Reference ===')
    printBoard(theBoard)
    print('==========================')
    print()

    #initiate all positions to  ' '
    for i in theBoard:
        theBoard[i] = ' '

    while gameStart :
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space? ' )

        move = movePos()

        while checkMoveValid( move ) == False:
            move = movePos()

        theBoard[move] = turn

        if checkWinner(theBoard, turn) :
            print('Player ' + turn + ' has win the game!!')
            printBoard(theBoard)
            gameStart = False
        else :
            if checkTied (theBoard):
                print('The Game Tied!')
                printBoard(theBoard)
                gameStart = False
            else:
                if turn == 'O':
                    turn = 'X'
                else:
                    turn = 'O'


if __name__ == "__main__":
    runTicTacToe()


