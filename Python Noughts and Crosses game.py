#~~~~ NOUGHTS AND CROSSES
#~~~~ SOPHIE M. MAXWELL
#~~~~ 30153698
#~~~~ 14/05/2017
import random

#Prints out the board
def drawBoard(board):


        # The board is an array which holds the information
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n')
    print('================')
    print('\n')

#LPlayer inputs whether they want to be X or O
def inputPlayerLetter():
    
    #Returns list with player1 piece as first, player2 piece as second
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        #Ask the player what piece they want to be
        letter = raw_input('Do you want to be X or O?')
        letter = letter.upper()

    #First element is player1, second is player2
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
#Randomly choose who goes first
def WhoGoesFirst():
    
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player'

# returns True if player chooses to play again
def playAgain():

        answer = raw_input('Do you want to play again? (yes or no)')
        answer = answer.lower().startswith('y')
        return answer
#makes the player move where the letter is chosen
def makeMove (board, letter, move):
    board[move] = letter
# Returns true if someone wins
def isWinner(bo, le):
    
    # bo = board, le = letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # horizontal top
    (bo[4] == le and bo[5] == le and bo[6] == le) or #horizontal middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or #horizontal bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or #Verticle left
    (bo[8] == le and bo[5] == le and bo[2] == le) or #Verticle middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or #Verticle right
    (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal
#Make a duplicate board and list as duplicate
def getBoardCopy(board) :
    
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
# is passed move is free, return true
def isSpaceFree(board, move):
    
    return board[move] == ' '
# Get the player to input move
def getPlayerMove(board) :
  
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = raw_input('Player1 What is your next move? (1-9) ')
    return int(move)
# Returns valid move from passed list on board
def chooseRandomMoveFromList (board, movesList) :
  
    # Return none if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
#f=get player 2s move
def getPlayer2Move(board) :
 
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = raw_input('Player2 What is your next move? (1-9) ')
    return int(move)
#return true if board full, if not false
def isBoardFull(board):
 
    isBoardFilled = True

    for i in range(1, 9):
        if isSpaceFree(board, i):
            isBoardFilled = False
    
    return isBoardFilled

print('Welcome to Noughts and Crosses Python Edition!')
while True:

    # Reset board
    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = WhoGoesFirst()
    #turn = 'player'
    print('The ' + turn + ' Will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player1 turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            print(' ')
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! Player 1 won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'
        else:
            # Player2 turn
            drawBoard(theBoard)
            move = getPlayer2Move(theBoard)
            print(' ')
            makeMove(theBoard, player2Letter, move)
            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('Hooray! Player2 has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
            break
        
