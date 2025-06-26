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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j)
            for i in range(3)
            for j in range(3)
            if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")

    new_board = [row[:] for row in board]

    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        # Rows, columns and diagonals
    lines = []
    lines.extend(board)  # Rows
    lines.extend([[board[i][j] for i in range(3)] for j in range(3)])  # Columns
    lines.append([board[i][i] for i in range(3)])  # Diagonal top-left to bottom-right
    lines.append([board[i][2 - i] for i in range(3)])  # Diagonal top-right to bottom-left

    for line in lines:
        if line == [X, X, X]:
            return X
        elif line == [O, O, O]:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    best_action = None
    if current_player == X:
        best_val = -math.inf
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_action = action
    else:
        best_val = math.inf
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_action = action

    return best_action

