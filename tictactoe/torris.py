#welcome to the best tic for tack game probably ever

board = [' ' for x in range (10)]
torris = input("do you want to play torus? True of False: ")
if torris == False:
    print("okay here we go")
else:
    print('bold choice')

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le) or
    #torris winning rules are below
    (bo[2] == le and bo[6] == le and bo[7] == le) or
    (bo[2] == le and bo[4] == le and bo[9] == le) or
    (bo[1] == le and bo[6] == le and bo[8] == le) or
    (bo[3] == le and bo[4] == le and bo[8] == le))


# def is_win_tor(bo, le):
#         if torris == True:
#             (bo[2] == le and bo[6] == le and bo[7] == le) or
#             (bo[2] == le and bo[4] == le and bo[9] == le) or
#             (bo[1] == le and bo[6] == le and bo[8] == le) or
#             (bo[3] == le and bo[4] == le and bo[8] == le))

def playerMove():
    run = True
    while run:
        move = input('please select a position play between 1 and 9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print('sorry, this is occupied')
            else:
                print('please choose between 1 and 9')
        except:
            print('please type a number')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
#choose winning or blocking opponent
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy,let):
                move = i
                return move

# picking corners
#     cornersOpen = []
#     for i in possibleMoves:
#         if i in [1,3,7,9]:
#             cornersOpen.append(i)
#     if len(cornersOpen) > 0:
#         move = selectRandom(cornersOpen)
#         return move
# pick center
    if 5 in possibleMoves:
        move = 5
        return move
#pick edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print('sup and and welcome. This is Torris Tick-tac-toe')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(is_winner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('did you just loose to a computer? you suck')
            break

        if not(is_winner(board, 'X')):
            move = compMove()
            if move == 0:
                print('tie game')

            else:
                insertLetter('O', move)
                print('Computer played in position', move, ':')
                printBoard(board)
        else:
            print('you, my friend, are a winner. Good job champ')
            break


    if isBoardFull(board):
        print('cats game')

main()
