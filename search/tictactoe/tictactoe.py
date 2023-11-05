"""
Tic Tac Toe Player
"""

import math
import copy
from queue import Empty

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
    x_count,o_count = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list_of_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                list_of_actions.append((i,j))
    return list_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not Valid Action')
    newboard = copy.deepcopy(board)
    row,col = action
    newboard[row][col] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Possible Combinations
    Combo_Possibilities = []
    Combo_Possibilities.append([(0,0),(1,1),(2,2)])
    Combo_Possibilities.append([(0,2),(1,1),(2,0)])
    for x in range(3):
        Combo_Possibilities.append([(x,0),(x,1),(x,2)])
        Combo_Possibilities.append([(0,x),(1,x),(2,x)])

    x_coordinates,o_coordinates = [],[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_coordinates.append((i,j))
            elif board[i][j] == O:
                o_coordinates.append((i,j))
    for combo in Combo_Possibilities:
        if all([value in x_coordinates for value in combo]):
            return X
        if all([value in o_coordinates for value in combo]):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Winning_Player = winner(board)
    if Winning_Player is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winning_Player = winner(board)
    if Winning_Player == X:
        return 1
    elif Winning_Player == O:
        return -1
    else:
        return 0

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,minvalue(result(board,action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)   
    x = math.inf
    for action in actions(board):
        x = min(x,maxvalue(result(board,action)))
    return x

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    result_set = dict()
    if player(board) == O: 
        for action in actions(board):
            result_set[action] = maxvalue(result(board,action))
        sort_list = dict(sorted(result_set.items(), key=lambda item: item[1]))
        decision = list(sort_list.keys())[0]
    elif player(board) == X:
        for action in actions(board):
            result_set[action] = minvalue(result(board,action))
        sort_list = dict(sorted(result_set.items(), key=lambda item: item[1]))
        decision = list(sort_list.keys())[-1]
    print(sort_list) 
    return decision
    
    
