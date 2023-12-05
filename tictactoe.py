"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, X],
            [X, O, X],
            [O, X, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for row in board:
        xCounter += row.count(X)
        oCounter += row.count(O)

    if(xCounter > oCounter):
        return O

    return X    

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add([i, j])

    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # if player(board) == X:
    #     board[action[0], action[1]] = X
    #     return board
        
    # board[action[0], action[1]] = O
    # return board

    print(action)

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X

    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    for row in board:
        if all(item == X for item in row):
            return X
        if all(item == O for item in row):
            return O

    for i in range(len(board)):
        xCounter = 0
        oCounter = 0
        for j in range(len(board[i])):
            if board[j][i] == X:
                xCounter += 1
            if board[j][i] == O:
                oCounter += 1
        if xCounter == 3:
            return X
        if oCounter == 3:
            return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    emptyCounter = 0
    for row in board:
        emptyCounter += row.count(EMPTY)
    if emptyCounter == 0:
        return True

    if board[0][0] == board[1][1] == board[2][2] == X or board[0][0] == board[1][1] == board[2][2] == O:
        return True

    if board[0][2] == board[1][1] == board[2][0] == X or board[0][2] == board[1][1] == board[2][0] == O:
        return True

    for row in board:
        if all(item == X for item in row) or all(item == O for item in row):
            return True

    for i in range(len(board)):
        xCounter = 0
        oCounter = 0
        for j in range(len(board[i])):
            if board[j][i] == X:
                xCounter += 1
            if board[j][i] == O:
                oCounter += 1
        if oCounter == 3 or xCounter == 3:
            return True

    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if board[0][0] == board[1][1] == board[2][2] == X:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == X:
        return 1

    if board[0][0] == board[1][1] == board[2][2] == O:
        return -1
    if board[0][2] == board[1][1] == board[2][0] == O:
        return -1
    
    for row in board:
        if all(item == X for item in row):
            return 1
        if all(item == O for item in row):
            return -1

    for i in range(len(board)):
        xCounter = 0
        oCounter = 0
        for j in range(len(board[i])):
            if board[j][i] == X:
                xCounter += 1
            if board[j][i] == O:
                oCounter += 1
        if xCounter == 3:
            return 1
        if oCounter == 3:
            return -1

    return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        return maxMove(board).action
        
    return minMove(board).action

    raise NotImplementedError


def maxMove(board):
    move = Move([], -1)

    if terminal(board):
        move.value = utility(board)
        return move

    for action in actions(board):
        move.action = action
        move = max(move, minMove(result(board, action)))

    return move


def max(move, minMove):
    if minMove.value > move.value:
        return minMove

    return move


def minMove(board):
    move = Move([], -1)

    if terminal(board):
        move.value = utility(board)

    for action in actions(board):
        move.action = action
        move = min(move, maxMove(result(board, action)))

    return move


def min(move, maxMove):
    if maxMove.value < move.value:
        return maxMove

    return move


class Move():
    def __init__(self, action, value):
        self.action = action
        self.value = value