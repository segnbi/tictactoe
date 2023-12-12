"""
Tic Tac Toe Player
"""

import math
import sys
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board = copy.deepcopy(board)

    if not any(action == validAction for validAction in actions(board)):
        raise Exception

    if terminal(board):
        return board

    if player(board) == X:
        board[action[0]][action[1]] = X
        return board
        
    board[action[0]][action[1]] = O
    return board


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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    emptyCounter = 0

    for row in board:
        emptyCounter += row.count(EMPTY)
        
    if emptyCounter == 0:
        return True

    if winner(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        return maxMove(board).action
        
    return minMove(board).action


def maxMove(board):
    move = Move([], -1)

    if terminal(board):
        move.value = utility(board)
        return move

    for action in actions(board):
        move = max(move, minMove(result(board, action)), action)

    return move


def max(move, minMove, action):
    if minMove.value > move.value:
        minMove.action = action
        return minMove

    return move


def minMove(board):
    move = Move([], 1)

    if terminal(board):
        move.value = utility(board)

    for action in actions(board):
        move = min(move, maxMove(result(board, action)), action)

    return move


def min(move, maxMove, action):
    if maxMove.value < move.value:
        maxMove.action = action
        return maxMove

    return move


class Move():
    def __init__(self, action, value):
        self.action = action
        self.value = value